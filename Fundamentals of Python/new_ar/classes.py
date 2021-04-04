from math import pi
print('Module with Rectangle, Square, and Circle classes is imported')
class Rectangle:
  def __init__(self, width=None, height=None):
    self.width = width
    self.height = height
    
  def __str__(self):
    return 'Rectangle'

  def calc_area(self):
    area = self.width * self.height
    return area
        
  def calc_perimeter(self):
    perimeter = self.width * 2 + self.height * 2
    return perimeter

class Square:
  def __init__(self, side=None):
    self.side = side

  def __str__(self):
    return 'Square'

  def calc_area(self):
    area = self.side**2
    return area
        
  def calc_perimeter(self):
    perimeter = self.side * 4
    return perimeter

class Circle:
  def __init__(self, radius=None):
    self.radius = radius
    
  def __str__(self):
    return 'Circle'

  def calc_area(self):
    s = pi * self.radius**2 
    return s
        
  def calc_perimeter(self):
    l = 2 * pi * self.radius
    return l