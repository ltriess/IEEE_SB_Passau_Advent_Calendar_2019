#!/usr/bin/env python3

import sys

DEBUG = False


def count_jump_positions(position: tuple, grid_size: tuple):
    px, py = position
    counter = 0
    for x in range(grid_size[0]):
        for y in range(grid_size[1]):
            if x == px or y == py or abs(x - px) == abs(y - py):
                # ignore all fields that involve walking horizontal, vertical or diagonal
                continue
            else:
                counter += 1

    return counter


def main():

    if DEBUG:
        sys.stdin = open("samples/05_input.txt")

    rows, columns = (int(i) for i in input().split(" "))

    if rows == 1 or columns == 1:
        # trivial case: no possible routes can be found
        print(0)
    else:
        # count the number of connections in a graph
        options = 0
        for row in range(rows):
            for column in range(columns):
                options += count_jump_positions(
                    position=(row, column), grid_size=(rows, columns)
                )

        # divide the number of graph connections by 2 to eliminate already visited positions
        # add the initial number of jump positions which is equal to the grid size
        print(options // 2 + rows * columns)


if __name__ == "__main__":
    main()
