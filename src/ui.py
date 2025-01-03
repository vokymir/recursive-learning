from group import Group


class UI:
    basefolder: str

    def __init__(self):
        pass

    def how_to_use(self):
        pass

    def which_group(self, groups: list[Group]) -> str:
        """
        Show user all groups and let him choose one.
        Return group ID.
        """
        string: str = "||"
        res: str

        for i in range(len(groups)):
            string += f" ({i}) {groups[i].g_name} |"
        string += "|"

        while 1:
            print(string)
            res = input("Plese select group, by entering assigned number: ")
            try:
                res = int(res)
                break
            except:
                continue

        return groups[res].g_id
