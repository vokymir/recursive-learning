from group import Group
from qna import QnA


class UI:
    basefolder: str

    def __init__(self):
        pass

    def how_to_use(self) -> None:
        string: str

        with open("howtouse", mode="r", encoding="utf-8") as f:
            string = f.read()

        print(string)

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

    def which_qna(self, qnas: list[QnA]) -> int:
        """
        Show user all QnAs and let him choose one.
        Return QnA ID.
        """
        string: str = "\n"
        res: str

        for i in range(len(qnas)):
            string += f"({qnas[i].id}) {qnas[i].question[:20]}{"..." if len(qnas[i].question) > 100 else ""} \n"

        print(string)
        print(
            "Plese select question by entering assigned number.\nIf you are unsure, you can expand any question by entering its number with 'ext', e.g. '0ext'."
        )
        while 1:
            res = input("Please select number: ")
            # show the question in greater detail
            if "ext" in res:
                left, right = res.split("ext")

                # for more flexibility either search for number on the left and right
                try:
                    left = int(left)
                    qna_left = None
                    for qna in qnas:
                        if qna.id == left:
                            qna_left = qna
                            break

                    if qna_left:
                        print(f"({qna_left.id}) {qna_left.question}")
                except:
                    try:
                        right = int(right)
                        qna_right = None
                        for qna in qnas:
                            if qna.id == left:
                                qna_right = qna
                                break

                        if qna_right:
                            print(f"({qna_right.id}) {qna_right.question}")
                    except:
                        print("Invalid expression...")
                finally:
                    continue
            # try getting a number out of input
            try:
                # is number
                res = int(res)
                # is an option?
                is_valid = False
                for qna in qnas:
                    if qna.id == res:
                        is_valid = True
                        break

                if is_valid:
                    break
            except:
                continue

        return res
