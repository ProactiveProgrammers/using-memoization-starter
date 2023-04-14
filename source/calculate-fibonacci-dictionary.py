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
    # TODO Read the following references reference:
    # https://zeptomath.com/tools/fibonaccinumbers.php?number=70&hl=en
    # https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula
    # https://medium.com/explorations-in-python/calculating-any-term-of-the-fibonacci-sequence-using-binets-formula-in-python-36e7e261d1d8
    # TODO: Note that this function is implemented for you; however,
    # you should make sure that you understand how this function works!
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
    # request the 70th fibonacci number while using the LRU cache
    fibonacci_value_70 = fibonacci(70)
    # confirm the calculation of Fibonacci number with Binet's equation
    fibonacci_value_binet_70 = fibonacci_binet(70)
    print(f"Recursive Fibonacci(70) = {fibonacci_value_70}")
    print(f"Binet Fibonacci(70)     = {fibonacci_value_binet_70}")
