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
        raise ValueError("Logarithm undefined for non-positive a.")
    if b <= 0 or b == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    else:
        math.log(a,b)

def exp(a, b): a^b


git add calculator.py	     # staging all files to be saved
git commit -m "modified calculator p1" # saving changes w/ message
git push