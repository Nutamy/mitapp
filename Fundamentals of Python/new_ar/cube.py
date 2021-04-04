
from square import *

print('Class Cube is imported successfully')

class Cube:

    def __init__(self, side=None):
        self.side = side

    def __str__(self):
        return f'Cube with side {self.side} cm'

    def get_surface_area(self):
        s = self.side**2 * 6
        return s

    def get_volume(self):
        v = self.side**3
        return v

    @staticmethod
    def get_info():
        return 'This class calculates surface area and volume of the cube.'