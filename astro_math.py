from math import floor, fabs


def fraction(x):
    """Get fraction of double

    :param x:
    :return:
    """
    return x - floor(x)


def modulo(x, y):
    """Get modulo of x/y

    :param x:
    :param y:
    :return:
    """
    return y * fraction(x / y)


def degree_to_decimal(degrees, minutes, seconds):
    """ Convert angles from degrees, minutes, second to decimal

    :param degrees: int
    :param minutes: int
    :param seconds: int
    :return: decimal
    """
    sign = -1.0 if degrees < 0 or minutes < 0 or seconds < 0 else 1.0
    return sign * (fabs(degrees) + fabs(minutes) / 60.0 + fabs(seconds) / 3600.0)


def decimal_to_degree(angle):
    """ Convert angles from decimal to degrees, minutes, second

    :param angle: float
    :return: tuple(int, int, float)
    """
    x = fabs(angle)
    degrees = int(x)
    minutes = int((x - degrees) * 60.0)
    seconds = (((x - degrees) * 60.0) - minutes) * 60.0
    return degrees, minutes, seconds
