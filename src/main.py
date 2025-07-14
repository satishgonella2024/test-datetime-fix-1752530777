def factorial(n):
    """
    Calculates the factorial of a given number using an iterative approach.
    
    Args:
        n (int): The number to calculate the factorial for.
    
    Returns:
        int: The factorial of the given number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result