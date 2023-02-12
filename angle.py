from angle_format import AngleFormat


class Angle:

    def __init__(self, alpha, angle_format=AngleFormat.DECIMAL):
        self.alpha = alpha
        self.angle_format = angle_format

    def format(self):
        print(f'degree_to_decimal, {self.alpha}')
