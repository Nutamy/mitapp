
print('Class Rectangle is imported successfully!!!!!!!!!!!')


class Rectangle:

    def __init__(self, width=None, height=None):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle with width {self.width} cm and height {self.height} cm'

    def get_area(self):
        area = self.width * self.height
        return area
        
    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter
    
    @staticmethod
    def get_info():
        return 'This class calculates perimeter and area of the rectangles.'
