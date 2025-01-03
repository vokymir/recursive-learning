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
