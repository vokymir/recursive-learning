from qna import QnA
from helper import Priority, GroupError

from pathlib import Path
import os
from datetime import date


class Group:
    """
    Encapsulation of Group in file.
    Holds info about it and serves as mediator who can directly access and edit file.
    """

    basefolder: str
    g_name: str
    g_id: str
    g_par_id: str
    g_priority: Priority
    next_qna_id: int

    def __init__(self, basefolder: str):
        self.basefolder = basefolder

    def create_group(
        self,
        g_name: str,
        g_id: str,
        g_par_id: str,
        g_priority: Priority = Priority.NORMAL,
    ) -> GroupError:
        """
        Create a new group with specified parameters.
        Save group to folder structure using save_group.
        """
        self.g_name = g_name
        self.g_id = g_id
        self.g_par_id = g_par_id
        self.g_priority = g_priority
        self.next_qna_id = 0

        return self.save_group()

    def save_group(self) -> GroupError:
        """
        Save self as group folder and file.
        """
        try:
            os.mkdir(os.path.join(self.basefolder, self.g_id))
        except:
            return GroupError.DIRECTORY_ALREADY_EXIST

        return self.save_group_info()

    def save_group_info(self) -> GroupError:
        """
        Go to group folder and save info about it into its .g file.
        Overwrite on exist.
        """
        try:
            with open(
                os.path.join(self.basefolder, self.g_id, self.g_id + ".g"),
                "w+",
                encoding="utf-8",
            ) as f:
                f.write(
                    f"{self.g_id}|{self.g_name}|{self.g_par_id}|{self.g_priority.value}|{self.next_qna_id}"
                )
        except:
            return GroupError.PATH_INVALID

        return GroupError.SUCCESS

    def load_group(self, g_id: str) -> GroupError:
        """
        Load existing group from file.
        Foldername is the same as group ID. Only loads attributes, not actual QnAs.
        Return true on success, false on failure.
        """
        try:
            with open(os.path.join(self.basefolder, g_id, g_id + ".g")) as f:
                (
                    self.g_id,
                    self.g_name,
                    self.g_par_id,
                    self.g_priority,
                    self.next_qna_id,
                ) = (
                    f.read().strip().split("|")
                )
            self.g_priority = Priority(int(self.g_priority))
            self.next_qna_id = int(self.next_qna_id)
            return GroupError.SUCCESS
        except:
            return GroupError.LOAD_FAILED

    def delete_group(self) -> GroupError:
        for i in range(1000):
            try:
                os.rename(
                    os.path.join(self.basefolder, self.g_id),
                    os.path.join(self.basefolder, self.g_id + ".gg" + f"{i:03}"),
                )
                return GroupError.SUCCESS
            except:
                pass
        return GroupError.DELETE_FAILED

    def save_qna(
        self, qna: QnA, give_new_id: bool = True, overwrite: bool = False
    ) -> bool:
        """
        Save an existing qna object to group folder where this qna doesn't exist.
        Return true on success, false on failure.
        """
        if give_new_id:
            qna.id = self.next_qna_id
        path = os.path.join(self.basefolder, self.g_id, f"{qna.id}.qna")
        if (not overwrite) and Path(path).exists():
            return GroupError.QNA_W_ID_ALREADY_EXIST

        string = "&^#\n".join(
            [
                f"{qna.id}",
                qna.question,
                qna.hint,
                qna.answer,
                str(qna.date_added.toordinal()),
                ",".join(qna.progress),
            ]
        )

        try:
            with open(
                path,
                "w+",
                encoding="utf-8",
            ) as f:
                f.write(string)

            if give_new_id:
                self.next_qna_id += 1
            if self.save_group_info() != GroupError.SUCCESS:
                return GroupError.SAVE_G_INFO_FAILED
            else:
                return GroupError.SUCCESS

        except:
            return GroupError.QNA_CREATE_FAILED

    def load_qna(self, qna_id: int) -> QnA | None:
        """
        Load QnA with qna_id ID from group folder.
        Returns QnA instance on success and None on failure.
        """
        path = Path(self.basefolder, self.g_id, f"{qna_id}.qna")
        content: list[str]
        qna: QnA = QnA()

        if not path.exists():
            return None

        with open(path, "r", encoding="utf-8") as f:
            content = f.read().split("&^#\n")

        qna.id = int(content[0])
        qna.question = content[1]
        qna.hint = content[2]
        qna.answer = content[3]
        qna.date_added = date.fromordinal(int(content[4]))
        qna.progress = content[5].split(",")

        return qna

    def edit_qna(self, qna: QnA) -> bool:
        """
        Edit QnA in group folder.
        Uses ID to recognize QnA, resaves it.
        Return true on success, false on failure.
        """
        return self.save_qna(qna, False, True)
