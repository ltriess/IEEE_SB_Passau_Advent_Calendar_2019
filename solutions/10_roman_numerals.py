#!/usr/bin/env python3

import sys
from itertools import combinations

DEBUG = False

r2i = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

i2r = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}

invalids = set()
known = r2i


def roman2int(roman):
    result = 0
    i = 0

    if roman in known:
        return known[roman]
    if roman in invalids:
        return None

    while i < len(roman):
        p1 = r2i.get(roman[i], 0)

        if i + 1 < len(roman):
            p2 = r2i.get(roman[i + 1], 0)
            if p1 >= p2:
                result += p1
                i += 1
            else:
                result += p2 - p1
                i += 2
        else:
            result += p1
            i += 1

    # check whether the roman numeral entered is valid
    if int2roman(result) == roman:
        known[roman] = result
        return result
    else:
        invalids.add(roman)
        return None


def int2roman(number):
    result = ""

    for value, numeral in sorted(i2r.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value

    return result


def main():

    if DEBUG:
        sys.stdin = open("samples/10_input.txt")

    lines = int(input())

    for _ in range(lines):
        line = input()

        inp = {line[x:y] for x, y in combinations(range(len(line) + 1), r=2)}
        numbers = sorted(n for n in map(roman2int, inp) if n is not None)
        print(len(numbers), " ".join(str(x) for x in numbers))


if __name__ == "__main__":
    main()
