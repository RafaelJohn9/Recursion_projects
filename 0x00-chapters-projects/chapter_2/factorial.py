#!/usr/bin/python3
"""
this is a recursive function used to get the factorials of numbers
"""


def factorial(n: int):
    """
    factorial function
    """
    # BASECASE
    if n < 2:
        return 1

    # RECURSIVE CASE
    answer = factorial(n - 1)

    return answer * n


if __name__ == "__main__":
    while True:
        num = int(input("please enter number: "))
        print(factorial(num))
