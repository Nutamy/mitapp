def add(x, y):
    return x + y

def sub(x, y):
    if x > y:
        x, y = y, x
    return y - x

def mult(x, y):
    return x * y

def div(x, y):
    if x > y:
        x, y = y, x
    return y // x

