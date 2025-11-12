"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b): a + b

def sub(a, b): a - b

def mul(a, b): a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by Zero")
    else:
        b / a

def log(a, b):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive x.")
    if b <= 0 or b == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    else:
        math.log(a,b)# use math library + raise ValueError

def exp(a, b): a^b
