"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

#https://github.com/DiegoCanas07/lab11-DC-EY.git
#Partner 1: Diego Canas
#Partner 2: Ethan Yin

import math
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def log(a,b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid logarithmic arguments")
    else:
        return math.log(b,a)

def exp(a,b):
    return a**b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by Zero")
    else:
        b / a

