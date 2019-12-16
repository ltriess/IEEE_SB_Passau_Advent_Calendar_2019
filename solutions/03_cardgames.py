#!/usr/bin/env python3

import math
import sys
from functools import reduce

DEBUG = False


def lcm(*numbers):
    def _lcm(a, b):
        return int(a * b / math.gcd(a, b))

    return reduce(_lcm, numbers)


def main():

    if DEBUG:
        sys.stdin = open("samples/03_input.txt")

    num_children = int(input())

    group_sizes = []
    for _ in range(num_children):
        input()  # group size
        group_sizes.append([int(i) for i in input().split(" ")])

    # find least common multiple for each child
    multiples = []
    for g in group_sizes:
        multiples.append(lcm(*g))

    # avoid disadvantage of some children
    maxval = max(multiples)
    for idx, m in enumerate(multiples):
        multiples[idx] = maxval // m * m

    print("\n".join([str(m) for m in multiples]))


if __name__ == "__main__":
    main()
