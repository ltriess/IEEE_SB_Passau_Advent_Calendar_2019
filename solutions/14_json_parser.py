#!/usr/bin/env python3

import json
import sys

DEBUG = False

alp = "abcdefghijklmnopqrstuvwxyz"


def check_valid(string, value):
    s = sum(alp.find(s) for s in string)
    return s > value


def search_dict(d, valid_keys, char_sum, out=None):
    if out is None:
        out = []

    for key in valid_keys:
        v = d[key]
        if isinstance(v, dict):
            search_dict(v, valid_keys, char_sum, out)
        else:
            # TODO: how to know which have to be excluded though key is correct?
            if (
                check_valid(v, char_sum)
                and v not in ["false", "foo", "bar", "baz"]
                and v[0].isupper()
            ):
                out.append(v)

    return out


def main():

    if DEBUG:
        sys.stdin = open("samples/14_input.txt")

    char_sum = int(input())
    num_keys = int(input())
    valid_keys = []
    for _ in range(num_keys):
        key = input()
        if check_valid(key, char_sum):
            valid_keys.append(key)

    input()  # empty line
    message = json.load(sys.stdin)

    out = search_dict(message, valid_keys, char_sum)

    print(" ".join(out))


if __name__ == "__main__":
    main()
