#!/usr/bin/env python3

import sys

DEBUG = False


def main():

    if DEBUG:
        sys.stdin = open("samples/23_input.txt")

    # Child's number: 0 ≤ m < n
    # Naughtiness: 0 ≤ o ≤ 1000  --> lower == better
    # Helpfulness: 0 ≤ p ≤ 1000  --> higher == better
    # Pray: 0 ≤ q ≤ 1000  --> higher == better
    # Crimes: 0 ≤ r ≤ 10  --> lower == better
    # Money: 0 ≤ s ≤ 1.000.000  --> lower == better

    num_children = int(input())

    children = []
    for _ in range(num_children):
        m, o, p, q, r, s = map(int, input().split(" "))
        children.append((o, 1000 - p, 1000 - q, r, s, m))

    children = sorted(children)

    for c in children:
        print(c[-1])


if __name__ == "__main__":
    main()
