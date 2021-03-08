from rectangle import *

print('Class Square is imported successfully')

class Square(Rectangle):

    def __init__(self, side=None):
        self.side = side
        super().__init__(width=self.side, height=self.side)

    def __str__(self):
        return f'Square with side {self.side} cm'

    def get_area(self):
        area = self.side**2
        return area
        
    def get_perimeter(self):
        perimeter = self.side * 4
        return perimeter
    
    @staticmethod
    def get_info():
        return 'This class calculates perimeter and area of the square.'
