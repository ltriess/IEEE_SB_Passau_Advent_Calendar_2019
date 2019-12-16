#!/usr/bin/env python3

import sys
from itertools import combinations

DEBUG = False


def main():

    if DEBUG:
        sys.stdin = open("samples/09_input.txt")

    tables = [int(x) for x in input().split(" ")]

    while True:
        try:
            n, t = map(int, input().split(" "))
            if any(map(lambda x: sum(x) == n, combinations(tables, t))):
                print("POSSIBLE")
            else:
                print("IMPOSSIBLE")
        except EOFError:
            break


if __name__ == "__main__":
    main()
