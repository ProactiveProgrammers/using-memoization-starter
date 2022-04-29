"""Calculate the Fibonacci sequence of numbers using an LRU cache."""

import functools
import math


@functools.lru_cache(maxsize=128)
def fibonacci(number: int) -> int:
    """Calculate a number in the Fibonacci sequence using recursion and an LRU cache."""
    # TODO: Consult the course slides and your textbook for a way in
    # which you can implement this function in a recursive fashion


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
    print(f"LRU cache information: {fibonacci.cache_info()}")
    # confirm the calculation of Fibonacci number with Binet's equation
    fibonacci_value_binet_100 = fibonacci_binet(100)
    print(f"Binet fibonacci(100) = {fibonacci_value_100}")
    # request the 150th fibonacci number while using the LRU cache
    fibonacci_value_150 = fibonacci(150)
    print(f"fibonacci(150) = {fibonacci_value_150}")
    print(f"LRU cache information: {fibonacci.cache_info()}")
    # confirm the calculation of Fibonacci number with Binet's equation
    fibonacci_value_binet_150 = fibonacci_binet(150)
    print(f"Binet fibonacci(150) = {fibonacci_value_150}")
