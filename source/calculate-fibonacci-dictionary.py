"""Calculate the Fibonacci sequence of numbers using a dictionary."""

import math

# TODO: create a dictionary to use as a cache for the fibonacci numbers


def fibonacci(number: int) -> int:
    """Calculate a number in the Fibonacci sequence using recursion and a dictionary."""
    # Reference:
    # https://stackoverflow.com/questions/61604632/fibonacci-function-memoization-in-python
    # TODO: Base case for 0: return 0
    # TODO: Base case for 1: return 1
    # TODO: Recursive case: only perform the computation when needed because
    # of the fact that the requested value is not in the dictionary
    # TODO: the value is in the dictionary, so look it up and return it
    # TODO: the value is not in the dictionary, so compute it and then
    # store it in the dictionary so that it can be used later
    # TODO: return the computed value of the fibonacci sequence


def fibonacci_binet(n: int) -> int:
    """Calculate a number in the Fibonacci sequence using Binet's formula."""
    # Reference:
    # https://zeptomath.com/tools/fibonaccinumbers.php?number=150&hl=en
    # https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula
    # https://medium.com/explorations-in-python/calculating-any-term-of-the-fibonacci-sequence-using-binets-formula-in-python-36e7e261d1d8
    square_root_n = math.sqrt(n)
    return int((((1 + square_root_n) ** n - (1 - square_root_n) ** n) / (2 ** n * square_root_n)))


if __name__ == "__main__":
    # request the 100th fibonacci number while using the LRU cache
    fibonacci_value_100 = fibonacci(100)
    print(f"Recursive fibonacci(100) = {fibonacci_value_100}")
    # confirm the calculation of Fibonacci number with Binet's equation
    fibonacci_value_binet_100 = fibonacci_binet(100)
    print(f"Binet fibonacci(100) = {fibonacci_value_100}")
    # request the 150th fibonacci number while using the LRU cache
    fibonacci_value_150 = fibonacci(150)
    print(f"fibonacci(150) = {fibonacci_value_150}")
    # confirm the calculation of Fibonacci number with Binet's equation
    fibonacci_value_binet_150 = fibonacci_binet(150)
    print(f"Binet fibonacci(150) = {fibonacci_value_150}")
