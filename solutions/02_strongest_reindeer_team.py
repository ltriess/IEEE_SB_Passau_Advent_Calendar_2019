#!/usr/bin/env python3

import sys

DEBUG = False


def max_sum_path(formation):
    total = formation[-1]

    # iterate from last to second row
    for i in range(2, len(formation) + 1):
        i = len(formation) - i
        for j in range(len(formation[i + 1]) - 1):
            total[j] = formation[i][j] + max(total[j], total[j + 1])

    return total[0]


def main():

    if DEBUG:
        sys.stdin = open("samples/02_input.txt")

    lines = int(input())

    reindeers = []
    for _ in range(lines):
        reindeers.append([int(x) for x in input().split(" ")])

    print(max_sum_path(reindeers))


if __name__ == "__main__":
    main()
