#!/usr/bin/env python3

import math
import sys

DEBUG = False


def check_line(elements):
    # check if solution is incomplete
    if "?" in elements:
        print(False)
        sys.exit(0)

    line = [int(i) for i in elements]

    # check for invalid values
    if max(line) > len(elements) or min(line) <= 0:
        print(False)
        sys.exit(0)

    # check if numbers are unique
    if len(line) > len(set(line)):
        print(False)
        sys.exit(0)


def main():

    if DEBUG:
        sys.stdin = open("samples/07_input.csv")

    sudoku_size = int(input().rstrip(";"))
    box_size = math.sqrt(sudoku_size)

    # check sudoku size
    if not (box_size - int(box_size)) == 0:
        print(False)
        sys.exit(0)

    # read matrix and check rows
    matrix = []
    for _ in range(sudoku_size):
        line = input().rstrip(";").split(",")

        check_line(line)
        matrix.append(line)

    # check columns
    for i in range(sudoku_size):
        check_line([row[i] for row in matrix])

    # check boxes
    box_size = int(box_size)
    for i in range(box_size):
        for j in range(box_size):
            # extract box
            box = [
                [matrix[i * box_size + m][j * box_size + n] for n in range(box_size)]
                for m in range(box_size)
            ]

            # flatten list of list
            box = [item for sublist in box for item in sublist]

            # check single box
            check_line(box)

    print(True)


if __name__ == "__main__":
    main()
