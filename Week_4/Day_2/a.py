


def add(a, b, c):
    return a + b + c

def subtract(a, b, c):
    return a - b - c

def multiply(a, b, c):
    return a * b * c

def divide(a, b, c):
    if b != 0 and c != 0:
        return a / b / c
    else:
        return " cannot divide by zero"
    
print(add(9,3,3))
print(subtract(9,3,3))
print(multiply(9,3,3))
print(divide(9,3,3))