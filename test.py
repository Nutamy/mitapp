""" tuple1 = (1,2,"Adam")
[print(x) for x in tuple1]
 """
""" dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'c':100, 'd':15, 'e':16}

dict1.update(dict2)
print(dict1)
print(dict2)



arr1 = [100,"Brad",-10,1,10.4,3,4,70,24,-9, "Hello", "How"]
arr2 = [100,-10,1,3,4,70,24,-9]

arr1.pop(1)
arr1.pop(-1)
arr1.pop(-1)
arr1.pop(3)
print(arr1) """

""" import csv
data = []
with open("./annual-enterprise-survey-2018-financial-year-provisional-csv.csv", 'r') as file:
# Начало вашего кода 
    data = list(csv.reader(file))
# Конец вашего кода
    u = set(data)
    print(u) """
""" def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

number = int(input("Enter the range of numbers: "))

result = []
start = 1
for num in range(start, number+1):
    result.append(fibonacci(num))
print(result)

    if n in (1, 2):
        return 1
    return fibonacci_num(n - 1) + fibonacci_num(n - 2)
 """


""" def sequence(n):
    result = []
    result.append(n)
    if n <= 0:
        return result
    else:
        return result + sequence(n-5)

print(sequence(16))
print(sequence(40))
 """



""" x = list(filter(lambda x: print(x), list(range(0,11,2))) """
""" def f(l):
    l2 =[]
    for i in l:
        if i%3 == 0:
            l2.append(i)
    return l2
l = list(range(0,50,3))
print(l) """

""" def polynomial(n, coef):
    # Начало вашего кода    
    for i in range(n+1):
        s = 0
        for j in coef:
            print('s={}'.format(s))
            print('i={}'.format(i))
            print('j={}'.format(j))
            s += j**i
    print(s)


polynomial(2, [1,2,3]) """
""" x = 2
y = [1, 2, 3]
print(polynomial(x, y)) """

""" test_dict = {'a': 10, 'p': 100, 'c': 0, 'b': 30}

def sort_dict(d):
    list_of_keys = []
    sorted_dict = {}
    for item in d.items():
        list_of_keys.append(item)
    list_of_keys.sort()
    for i in list_of_keys:
        sorted_dict[i] = d[i]
    return sorted_dict

result = sort_dict(test_dict)
print(result)


dt = {}
for i in range(10):
    for j in range(10):
        dt[j] = i
print(dt) """
""" def dog_ages_converter(dog_age):
    human_age = 0
    for age in range(dog_age):
        if age < 2:
            human_age += 10.5
        elif age >= 2:
            human_age += 4
    return int(human_age)
test = dog_ages_converter(12)
print(test) """
""" def how_many_days_in_months(month):
    if month.title() in ['January', 'March', 'May', 'July', 'August', 'October', 'December', 'Январь', 'Март', 'Май', 'Июль', 'Август', 'Октябрь', 'Декабрь']:
        return 'There are 31 days in {}'.format(month.title())
    elif month.title() in ['April', 'June', 'September', 'November', 'Апрель', 'Июнь', 'Сентябрь', 'Ноябрь']:
        return 'There are 30 days in {}'.format(month.title())
    elif month.title() in ['February', 'Февраль']:
        return 'There are 28/29 days in {}'.format(month.title())
print(how_many_days_in_months('sePTEmber')) """
for a,b,c in [1,2,3],[30,20,10],[400,500,600]:
    print('a:{}\nb:{}\nc:{}'.format(a,b,c))

for a in [1,2,3] 


















""" n = int(input())
for i in range(1, n+1):
    print(i, end='')



from math import pi
r = float(input())
v =(4/3) * pi * r**3
print(v) """

""" 
n = input()
print(int(n)+int(n+n)+int(n+n+n))
 """
""" f = float(input()) * 30.48
d = float(input()) * 2.54
sm = f + d
print(sm) """
""" a = float(input())
b = float(input())
c = (a**2 + b**2)**(1/2)
print(c) """
""" import numpy as np
a = np.array([[0, 1, 2], [4, 5, 6]])
a = a.transpose()
arr1 = [100,"Brad",-10,1,10.4,3,4,70,24,-9, "Hello", "How"]
arr2 = [100,-10,1,3,4,70,24,-9]
arr3 = [100,-10,1,3,10,4,70,24,-9]
arr4 = [[1,2,3],[4,5,6]]
arr5 = [[1,4],[2,5],[3,6]]

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5) """

""" arr1.clear()
arr1.extend(arr2)
print(arr1)
arrt = []
arrt=[[n[i] for n in arr4] for i in range(len(arr4[0]))]
arr4.clear()
arr4.extend(arrt)
print(arr4) """
""" Используя все возможные функции, преобразуйте arr1 в arr2. """
""" for i in range(len(arr3)):
    for j in range(len(arr3)-i-1):
        if arr3[j] < arr3[j+1]:
            arr3[j], arr3[j+1] = arr3[j+1], arr3[j]
print(arr3) """













""" x = 0
s = 0
y = 101
while x < y:
    if x % 2 == s:
        print(x)
        if x == 100:
            x = 101
            s = 1
            y = 1000
            print(101)
    x += 1   """

""" for a in range(0, 1000, 2):
    if a < 100:
        print(a)
    else:
        print(a+1) """

""" Trusted
Jupyter Server: local
Python 3: Not Started
1) Для заданного целого числа n выполнить следующие условные действия:

Если n нечетно, выведите Astana

Если n чётно и находится в диапазоне от 2 до 5, выведите Алматы

Если n чётно и находится в диапазоне от 6 до 20 включительно, выведите Astana

Если n чётно и больше 20, выведите Алматы """

""" n = int(input())
if n % 2 == 1:
    print('Astana')
elif n % 2 == 0:
    if 2 <= n <= 5:
        print('Алматы')
    elif 6 <= n <= 20:
        print('Astana')
    elif n > 20:
        print('Алматы')  """
