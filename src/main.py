from group import Group
from qna import QnA
from ui import UI
from logic import Logic
import helper

from datetime import date
import os
import sys


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


def main() -> int:
    basefolder: str
    intervals_s: str
    intervals: list[int]
    arguments: list[str]

    basefolder, intervals_s = get_config("config")
    intervals = [int(interval) for interval in intervals_s.strip().split(",")]

    arguments = sys.argv

    logic: Logic = Logic(basefolder, intervals)
    logic.parse_args(arguments)

    return 0


if __name__ == "__main__":
    main()
