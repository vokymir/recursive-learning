import os

from ui import UI
from group import Group
from qna import QnA
from helper import GroupError


class Logic:
    basefolder: str
    intervals: list[int]
    ui: UI
    groups: list[Group] = []

    def __init__(self, basefolder: str, intervals: list[int]):
        self.basefolder = basefolder
        self.intervals = intervals
        self.ui = UI()
        self.groups = []

    def parse_args(self, args: list[str]) -> bool:
        """
        Parse all arguments and do what they say.
        Return True on success, False on failure.
        """
        should_compile: bool = False
        should_run: bool = False
        should_add_qna: bool = False
        should_add_qroup: bool = False
        should_edit_qna: bool = False
        should_edit_group: bool = False
        should_del_group: bool = False
        should_del_qna: bool = False
        skip: bool = False

        for i in range(len(args)):
            if skip:
                continue

            arg = args[i]

            match arg:
                case "-c":
                    should_compile = True
                    break

                case "-r":
                    should_run = True
                    break

                case "-a":
                    should_add_qna = True
                    break

                case "-g":
                    should_add_qroup = True
                    break

                case "-e":
                    should_edit_qna = True
                    break

                case "-ge":
                    should_edit_group = True
                    break

                case "-d":
                    should_del_qna = True
                    break

                case "-gd":
                    should_del_group = True
                    break

                case _:
                    self.ui.how_to_use()
                    return False

        if should_del_group:
            self.del_group()
        if should_del_qna:
            self.del_qna()
        if should_edit_group:
            self.edit_group()
        if should_edit_qna:
            self.edit_qna()
        if should_add_qroup:
            self.add_group()
        if should_add_qna:
            self.add_qna()
        if should_compile:
            self.compile()
        if should_run:
            self.run_qnas()

        return True

    def load_groups(self) -> bool:
        """
        Load all groups and saves them into self.groups
        Return True on success, False on failure.
        """
        self.groups = list()

        for filename in os.listdir(self.basefolder):
            # exclude other files
            if ".gg" in filename:
                continue
            # load group
            g: Group = Group(self.basefolder)
            # check if valid
            if not g.load_group(filename):
                return False
            # add to arr
            self.groups.append(g)

        return True

    def del_group(self) -> bool:
        """
        Delete group specified by user.
        Call UI to ask user which group.
        Return True on success, False on failure.
        """
        # make sure groups are complete
        if len(self.groups) == 0:
            self.load_groups()
        # ask for group
        group_id = self.ui.which_group(self.groups)
        # delete group and check
        g = Group(self.basefolder)
        if g.load_group(group_id) != GroupError.SUCCESS:
            return False
        if g.delete_group() != GroupError.SUCCESS:
            return False
        # all done
        return True

    def load_qnas(self, g: Group) -> list[QnA]:
        qnas: list[QnA] = []
        path = os.path.join(self.basefolder, g.g_id)
        files = os.listdir(path)

        # check all files
        for file in files:
            if not ".qna" in file:
                continue
            # load QnA
            qna = g.load_qna(int(file.split(".")[0]))
            if qna != None:
                qnas.append(qna)

        return qnas

    def del_qna(self) -> bool:
        """
        Delete QnA specified by user.
        Ask user which group and which QnA ID in that group.
        Return True on succes, False on failure.
        """
        # make sure groups are complete
        if len(self.groups) == 0:
            self.load_groups()

        # get group
        g_id = self.ui.which_group(self.groups)
        g = Group(self.basefolder)
        ger = g.load_group(g_id)
        if ger != GroupError.SUCCESS:
            return False

        # get QnA
        qna_id = self.ui.which_qna(self.load_qnas(g))
        qna = g.load_qna(qna_id)
        if qna == None:
            return False

        # delete QnA
        if not g.del_qna(qna):
            return False

        return True

    def edit_group(self) -> bool:
        pass

    def edit_qna(self) -> bool:
        pass

    def add_group(self) -> bool:
        pass

    def add_qna(self) -> bool:
        pass

    def compile(self) -> bool:
        """
        Compile all groups into one file with only relevant QnAs.
        """
        pass

    def run_qnas(self) -> bool:
        """
        Open compiled file and show user one question after another.
        """
        pass
