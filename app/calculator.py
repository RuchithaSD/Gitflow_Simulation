def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division error: Denominator cannot be zero")
    return a / b


def power(a, b):
    return a ** b