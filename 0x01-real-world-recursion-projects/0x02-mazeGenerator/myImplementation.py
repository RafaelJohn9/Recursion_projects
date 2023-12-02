#!/usr/bin/python3

"""
my block generator
"""

def block(size=2):
    """
    returns  a block of the size given
    """
    block = {}

    for x in range(size):
        for y in range(size):
            block[(x,y)] = chr(9608)
    return block

def cutter():














if __name__ == '__main__':
    size = 10
    myBlock = block(size)
    for i in range(size):
        for j in range(size):
            print(myBlock[(i,j)], end="")
        print()
