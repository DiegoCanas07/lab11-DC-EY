#https://github.com/DiegoCanas07/lab11-DC-EY.git
#Partner 1: Diego Canas
#Partner 2: Ethan Yin
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def mul(a,b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithmic arguments")
    return math.log(b, a)

def exp(a,b):
    return a**b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by Zero")
    else:
        return a/ b

