from qna import QnA
from helper import Priority, GroupError

import os


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

    def save_qna(self, qna: QnA) -> bool:
        """
        Save an existing qna object to group folder.
        Return true on success, false on failure.
        """
        pass

    def load_qna(self, qna_id: int) -> QnA | None:
        """
        Load QnA with qna_id ID from group folder.
        Returns QnA instance on success and None on failure.
        """
        pass

    def edit_qna(self, qna: QnA) -> bool:
        """
        Edit QnA in group folder.
        Uses ID to recognize QnA, resaves it.
        Return true on success, false on failure.
        """
        pass