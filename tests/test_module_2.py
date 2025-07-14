{
    "code": "import math

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('Input must be a non-negative integer')
    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)",
    "tests": "# Tests are provided in the test suite",
    "documentation": "This function calculates the factorial of a given non-negative integer number. It uses recursion to compute the factorial by multiplying the number with the factorial of the number minus one. It also handles edge cases by raising a ValueError if the input is not a non-negative integer.",
    "dependencies": ["math"]
}