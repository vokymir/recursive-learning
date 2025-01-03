from enum import Enum


class Priority(Enum):
    LOW = 1
    NORMAL = 10
    HIGH = 100


class GroupError(Enum):
    SUCCESS = 0
    DIRECTORY_ALREADY_EXIST = 1
    PATH_INVALID = 2
    DELETE_FAILED = 3
    LOAD_FAILED = 4
    QNA_CREATE_FAILED = 5
    SAVE_G_INFO_FAILED = 6
    QNA_W_ID_ALREADY_EXIST = 7
    QNA_W_ID_DOESNT_EXIST = 8
    INVALID_PARAMS = 9
