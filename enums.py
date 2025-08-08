# enums.py

from enum import Enum

class CellState(Enum):
    EMPTY = 0
    GIVEN = 1
    USER_INPUT = 2
    SOLVING = 3
