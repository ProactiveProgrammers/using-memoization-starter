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
    # https://zeptomath.com/tools/fibonaccinumbers.php?number=70&hl=en
    # https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula
    # https://medium.com/explorations-in-python/calculating-any-term-of-the-fibonacci-sequence-using-binets-formula-in-python-36e7e261d1d8
    square_root_five = math.sqrt(5)
    coefficient = (1 / square_root_five)
    first_term = ((1 + square_root_five) / 2) ** n
    second_term = ((1 - square_root_five) / 2) ** n
    return int(coefficient * (first_term - second_term))


if __name__ == "__main__":
    # request the 35th fibonacci number while using the LRU cache
    fibonacci_value_35 = fibonacci(35)
    print(f"Recursive Fibonacci(35) = {fibonacci_value_35}")
    # confirm the calculation of Fibonacci number with Binet's equation
    fibonacci_value_binet_35 = fibonacci_binet(35)
    print(f"Binet Fibonacci(35)     = {fibonacci_value_binet_35}")
    print(f"LRU cache information: {fibonacci.cache_info()}")
    # request the 70th fibonacci number while using the LRU cache
    fibonacci_value_70 = fibonacci(70)
    # confirm the calculation of Fibonacci number with Binet's equation
    fibonacci_value_binet_70 = fibonacci_binet(70)
    print(f"Recursive Fibonacci(70) = {fibonacci_value_70}")
    print(f"Binet Fibonacci(70)     = {fibonacci_value_binet_70}")
    print(f"LRU cache information: {fibonacci.cache_info()}")
