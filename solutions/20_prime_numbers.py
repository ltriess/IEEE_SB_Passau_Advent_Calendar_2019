#!/usr/bin/env python3

import random
import sys

DEBUG = False


def is_prime(n):
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    def trial_composite(x):
        if pow(x, d, n) == 1:
            return False
        for j in range(s):
            if pow(x, 2 ** j * d, n) == n - 1:
                return False
        return True

    for _ in range(16):
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True


def main():

    if DEBUG:
        sys.stdin = open("samples/20_input.txt")

    for _ in range(int(input())):
        n = int(input())

        if n < 2:
            p = False
        elif n in [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]:
            p = True
        elif n % 2 == 0:
            p = False
        elif n < 100000000:
            p = True
            for i in range(2, n // 2):
                if n % i == 0:
                    p = False
                    break
        else:
            p = is_prime(n)

        print(str(p).lower())


if __name__ == "__main__":
    main()
