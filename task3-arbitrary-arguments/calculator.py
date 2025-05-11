"""
calculator.py

A script that provides a flexible calculator using arbitrary positional (*args)
and keyword (**kwargs) arguments. It supports operations such as addition,
subtraction, multiplication, and division with detailed error handling.
"""

def add(*args):
    """Returns the sum of all arguments."""
    return sum(args)

def subtract(*args):
    """Subtracts all subsequent numbers from the first number."""
    if not args:
        raise ValueError("At least one argument is required for subtraction.")
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    """Returns the product of all arguments."""
    if not args:
        raise ValueError("At least one argument is required for multiplication.")
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    """Divides the first number by each of the subsequent numbers in order."""
    if not args:
        raise ValueError("At least one argument is required for division.")
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Division by zero is undefined.")
        result /= num
    return result

def calculate(*args, **kwargs):
    """
    Performs a calculation based on the 'operation' specified in kwargs
    using the positional arguments provided in *args.

    Parameters:
    *args: numbers to operate on
    **kwargs: must include 'operation' (str): 'add', 'subtract', 'multiply', 'divide'

    Returns:
        Result of the calculation

    Raises:
        ValueError: if operation is not specified or invalid
    """
    operation = kwargs.get('operation')
    if not operation:
        raise ValueError("No operation specified. Use operation='add'/'subtract'/'multiply'/'divide'.")

    operations_map = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    func = operations_map.get(operation.lower())
    if not func:
        raise ValueError(f"Unsupported operation '{operation}'. Supported: add, subtract, multiply, divide.")

    return func(*args)

# Example usage
if __name__ == "__main__":
    try:
        print("Add:", calculate(1, 2, 3, 4, operation='add'))
        print("Subtract:", calculate(10, 3, 2, operation='subtract'))
        print("Multiply:", calculate(2, 5, operation='multiply'))
        print("Divide:", calculate(100, 5, 2, operation='divide'))
    except Exception as e:
        print("Error:", e)
