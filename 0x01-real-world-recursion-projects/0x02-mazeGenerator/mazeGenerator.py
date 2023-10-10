#!/usr/bin/python3

"""
a recursive code that is used to create a maze generator
"""

import random

WIDTH = 39 # Width of the maze (must be odd)
HEIGHT = 19 # Height of the maze (must be odd)
assert WIDTH % 2 == 1 and WIDTH >= 3
assert HEIGHT % 2 == 1 and HEIGHT >= 3
SEED = 1
random.seed(SEED)

# CHARACTERS TO BE USED IN DISPLAYING maze
EMPTY = ' '
MARK = '@'
WALL = chr(9608) # the block character
NORTH, SOUTH, EAST, WEST = 'n', 's', 'e','w'

# fill the maze character inside the maze
maze = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        maze[(x, y)] = WALL # every space is a wall at first

# prints the maze
def printMaze(maze, markX=None, markY=None):
    """ Displays the maze data structure in the maze argument.
    The markX and markY arguments are coordinates of the current
    '@' location of the algorithm as it generates the maze. """

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if markX == x and markY == y:
                # display the '@' mark here:
                print(MARK, end='')
            else:
                # Display the wall or empty space"
                print(maze[x,y], end='')
        print()

def visit(x, y):
    """ Carve out" empty spaces in the maze at x, y and then recursively
    move to neighbouring unvisited spaces. This function backtracks
    when the mark has reached a dead end """
    maze[(x, y)] = EMPTY
    printMaze(maze, x, y)
    print("\n\n")

    while True:
        # Check which neighbouring spaces adjacent to
        # the mark have not been visited already:
        unvisitedNeighbors = []

        if y > 1 and (x, y - 2) not in hasVisited:
            unvisitedNeighbors.append(NORTH)

        if y < HEIGHT - 2 and (x, y + 2) not in hasVisited:
            unvisitedNeighbors.append(SOUTH)

        if x > 1 and (x - 2, y) not in hasVisited:
            unvisitedNeighbors.append(WEST)

        if x < WIDTH - 2 and (x + 2, y) not in hasVisited:
            unvisitedNeighbors.append(EAST)

        if len(unvisitedNeighbors) == 0:
            # BASECASE
            # ALL NEIGHBORING SPACES HAVE BEEN VISITED
            # DEAD END. BACKTRACK TO AN EARLIER SPACE
            return
        else:
            # RECURSIVE CASE
            # randomly pick an unvisited neighbour to visit
            nextIntersection = random.choice(unvisitedNeighbors)

            # move the mark to an unvisited neighboring space
            if nextIntersection == NORTH:
                nextX = x
                nextY = y - 2
                maze[(x, y - 1)] = EMPTY
            elif nextIntersection == SOUTH:
                nextX = x
                nextY = y + 2
                maze[(x, y + 1)] = EMPTY
            elif nextIntersection == WEST:
                nextX = x - 2
                nextY = y
                maze[(x - 1, y)] = EMPTY
            elif nextIntersection == EAST:
                nextX = x + 2
                nextY = y
                maze[(x + 1, y)] = EMPTY

            hasVisited.append((nextX, nextY))
            visit(nextX, nextY)

hasVisited = [(1,1)]
visit(1, 1)

# display the final resulting maze data structure
printMaze(maze)
