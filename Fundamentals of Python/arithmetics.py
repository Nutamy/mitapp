

def add(a, b):
    return a + b

def subtract(a, b):
    c = 0
    if a > b :
        c = a - b
        if c < 0:
            return c * (-1)
        else:
            return c
    else:
        c = b - a
        if c < 0:
            return c * (-1)
        else:
            return c

def divide(a, b):
    if a > b:
        if b == 0:
            return 'Zero division error! Not Zorro! But Zero, sorry. Keep calm and try again.'
        else:
            return a // b
    else:
        if a == 0:
            return 'Zero division error! Not Zorro! But Zero, sorry. Keep calm and try again.'
        else:
            return b // a
    

def multiply(a, b):
    return a * b

def rem(a, b):
    if a > b:
        return a % b
    else:
        return b % a
        
def test(pred, ref):
    if pred == ref:
        return True
    else:
        return False
  
print('Arithmetics module is imported')

'''
1. add(a, b) - возвращает сумму двух чисел
2. subtract(a, b) - возвращает **абсолютную** разницу двух чисел
3. divide(a, b) - возвращает целочисленное деление большего числа на меньшее число
4. multiply(a, b) - возвращает произведение двух чисел
'''