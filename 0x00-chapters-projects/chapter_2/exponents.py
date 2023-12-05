#!/usr/bin/python3

"""
this is  a module that contain the exponent function
"""

def exponent(num, power):
    """
    exponent function done recursively
    """
    # BASECASE
    if power == 1:
        return num

    # RECURSIVE CASE
    ans = exponent(num, power - 1)
    return num * ans

if __name__ == "__main__":
    userinput_1 = int(input("Enter num: "))
    userinput_2 = int(input("Enter power: "))
    print(exponent(userinput_1, userinput_2))
