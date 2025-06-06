
import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error: Division by zero" if b == 0 else a / b
def power(a, b): return a ** b
def square_root(a): return "Error" if a < 0 else math.sqrt(a)
def modulo(a, b):
    """Return the remainder of ``a`` divided by ``b``.

    If ``b`` is ``0`` this function mimics ``divide`` by returning a
    human-readable error message instead of raising ``ZeroDivisionError``.
    """
    return "Error: Division by zero" if b == 0 else a % b
def factorial(a): return "Error" if a < 0 or not float(a).is_integer() else math.factorial(int(a))
def percentage(total, percent): return (total * percent) / 100
