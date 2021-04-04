from datetime import datetime
from datetime import timedelta 
from math import floor
y = 0
m = 0
d = 0
start = ''
while start == '':
    try:
        start = input('2021-03-08 type the date of start in format.\nAnswer: ')
    except:
        print('Use form pls.')


da = int(input('How many days do you have for doing it?\nAnswer: '))
parts = 0
while parts == 0:
    try:
        parts = int(input('How many parts it has? Example it has 22 lessons, type only numbers: 22\nAnswer: '))
    except:
        print('Type only numbers please.')

lesson = floor(da/parts)
iter_date = datetime.strptime(start, '%Y-%m-%d')
for i in range(parts):
    pri = iter_date.strftime('%b %d %Y')
    print(f'{i}: {pri}')
    iter_date = iter_date + timedelta(days=lesson)


start_list = start.split('-')
print(f'start_list:{start_list}')
print(f'start:{start}')



d = (datetime.now() - datetime.strptime('2020-01-01', '%Y-%m-%d')).days
end = datetime.strptime('2020-01-01', '%Y-%m-%d') + timedelta(days=da)
print(f'end:{end}')
print(d)

""" y = input('How many years do you have for doing it?\nAnswer: ')
m = input('How many monthes do you have for doing it?\nAnswer: ') """