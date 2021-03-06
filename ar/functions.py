import csv
from classes import *
print('Module with read_file, get_perimeters, and get_areas functions is imported')
def read_file(filename=None):
  list_of_figures = []
  with open(filename) as file:
    content = list(csv.reader(file, delimiter = ","))
    for row in content:
        if row[0].title() == 'Rectangle':
            if row[1] == row[2]:
                list_of_figures.append(Square(side=int(row[1])))
            else:
                list_of_figures.append(Rectangle(width=int(row[1]), height=int(row[2])))
        elif row[0].title() == 'Square':
            list_of_figures.append(Square(side=int(row[1])))
        elif row[0].title() == 'Circle':
            list_of_figures.append(Circle(radius=int(row[1])))
        else:
          print(f'{row[0].title()} is unknown figure')
  return list_of_figures


def get_perimeters(list_of_figures):
  for object in list_of_figures:
    p = object.calc_perimeter()
    print('{object} has following perimeter: {p:.2f}:'.format(object = object, p = p))


def get_areas(list_of_figures):
  for object in list_of_figures:
    area = object.calc_area()
    print('{object} has following area: {area:.2f}'.format(object = object, area = area))