from angle import Angle
from astro_constants import *
from astro_math import *


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def functions_test():
    # Use a breakpoint in the code line below to debug your script.
    print(f'modulo, {modulo(9, 5)}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'degree_to_decimal, {degree_to_decimal(15, 30, 0)}')
    print(f'degree_to_decimal, {decimal_to_degree(15.5)}')


def angle_test():
    angle = Angle(15.5)
    print(f'angle_to_decimal, {angle.format()}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # functions_test()
    angle_test()
