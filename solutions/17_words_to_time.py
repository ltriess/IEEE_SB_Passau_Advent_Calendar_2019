#!/usr/bin/env python3

import sys

DEBUG = False


def str2num(s):
    lookup = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty-one",
        "twenty-two",
        "twenty-three",
        "twenty-four",
        "twenty-five",
        "twenty-six",
        "twenty-seven",
        "twenty-eight",
        "twenty-nine",
    ]

    return lookup.index(s)


def main():

    if DEBUG:
        sys.stdin = open("samples/17_input.txt")

    inp = input().split(" ")

    # check the overall hour
    if "midnight" in inp:
        h = 0
    elif "o'clock" in inp:
        h = str2num(inp[inp.index("o'clock") - 1])
    else:
        h = str2num(inp[-1])

    # check the overall minutes
    m = 0
    if "quarter" in inp:
        d = inp[inp.index("quarter") + 1]
        if d == "to":
            m = 45
            h = (h - 1) % 24  # correct hour
        elif d == "past":
            m = 15
        else:
            raise ValueError
    elif "half" in inp:
        m = 30

    # check the precise minutes
    if "minutes" in inp:
        num = sum(str2num(inp[i]) for i in range(inp.index("minutes")))
        d = inp[inp.index("minutes") + 1]
        if d == "to":
            if m == 0:
                h = (h - 1) % 24  # correct hour
                m = 60
            assert m > num
            m = m - num
        elif d == "past":
            m += num
            assert m < 60
        else:
            raise ValueError

    print("{hour:02d}:{minute:02d}".format(hour=h, minute=m))


if __name__ == "__main__":
    main()
