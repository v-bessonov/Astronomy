from enum import Enum


class AngleFormat(Enum):
    """
    Angle format
    """
    DECIMAL = 1
    DEGREE_MINUTES = 2
    DEGREE_MINUTES_DECIMAL = 3
    DEGREE_MINUTES_SECONDS = 4
    DEGREE_MINUTES_SECONDS_DECIMAL = 5

