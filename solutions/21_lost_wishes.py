#!/usr/bin/env python3

import sys
from functools import reduce
from itertools import islice

DEBUG = True


def index(xs):
    # item at given (zero-based) index
    return (
        lambda n: None
        if 0 > n
        else (xs[n] if (hasattr(xs, "__getitem__")) else next(islice(xs, n, None)))
    )


def iterate(f):
    # infinite list of repeated applications of f to x
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)

    return lambda x: go(x)


def crc32(s):
    # CRC-32 checksum for an ASCII encoded string

    def go(x):
        x2 = x >> 1
        return 0xEDB88320 ^ x2 if x & 1 else x2

    table = [index(iterate(go)(n))(8) for n in range(0, 256)]

    return (
        reduce(lambda a, c: (a >> 8) ^ table[(a ^ ord(c)) & 0xFF], list(s), 0xFFFFFFFF)
        ^ 0xFFFFFFFF
    )


def main():

    if DEBUG:
        sys.stdin = open("samples/21_input.txt")

    # TODO: how to deal with German Umlaut (Ä, Ö, Ü)?

    for _ in range(int(input())):
        crc, data = input().split(" ")

        sentence = ""
        for i in range(0, len(data), 2):
            a = data[i : i + 2]
            if a == "__":
                sentence += "?"  # need to find this character

            else:
                sentence += chr(int(a, 16))

        _crc = crc32(sentence)
        print("{0} --> {1} --> {2}".format(crc, sentence, str(hex(_crc)).upper()[2:]))

    raise NotImplementedError("Actually easy, but  ä, ö, ü mess up my method...")


if __name__ == "__main__":
    main()
