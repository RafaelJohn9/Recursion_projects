#!/usr/bin/python3
"""
a module that contains the fibonacci function
"""
import functools

@functools.lru_cache()
def fibonacci(n:int):
    """
    this is a fibonacci function that is done
    recursively
    @n: for the nth sequence
    """
    # BASECASE
    if n <= 2:
        return 1

    # RECURSIVE CASE
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    """
    testcase
    """
    while (True):
        num =  int(input("Enter num: "))
        for i in range(1, num + 1):
            print(fibonacci(i), end=", ")

        print()
