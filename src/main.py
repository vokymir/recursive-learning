from group import Group
from qna import QnA

import os


def get_config(config_name: str) -> list[str]:
    """
    Open config file and return list of data from it.
    For now the data is basefolder of qna and intervals of repetition.
    """
    cwd: str = os.getcwd()
    config_path: str = os.path.join(cwd, config_name)
    file_content: str = ""
    basefolder: str = ""
    intervals: str = ""

    with open(config_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    basefolder = file_content[
        file_content.find("BASEFOLDER") + 11 : file_content.find("+ENDBASEFOLDER")
    ]

    intervals = file_content[
        file_content.find("INTERVALS") + 10 : file_content.find("+ENDINTERVALS")
    ]

    return [basefolder, intervals]


def main():
    basefolder: str
    intervals_s: str
    intervals: list[int]

    basefolder, intervals_s = get_config("config")
    intervals = [int(interval) for interval in intervals_s.strip().split(",")]

    g: Group = Group(basefolder)
    g.load_group("moje")

    print(g.g_name)


if __name__ == "__main__":
    main()
