def add(a, b):
    return a + b

import mymath  # Import my  custom module
print("Add:", mymath.add(5, 3))



def subtract(a, b):
    return a - b

import mymath  # Import my  custom module
print("Subtract:", mymath.subtract(10, 4))



def multiply(a, b):
    return a * b
import mymath  # Import my  custom module
print("Multiply:", mymath.multiply(6, 2))


def divide(a, b):
    if b == 0:
        return "Cannot divide by 0"
    return a / b
import mymath  # Import my  custom module
print("Divide:", mymath.divide(12, 3))


def square(n):
    return n ** 2
import mymath  # Import my  custom module
print("Square:", mymath.square(7))



def cube(n):
    return n ** 3
import mymath  # Import my  custom module
print("Cube:", mymath.cube(4))


