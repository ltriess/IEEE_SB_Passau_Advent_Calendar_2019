#!/usr/bin/env python3

import sys

DEBUG = False


def levenshtein_distance(s1, s2):

    if s1 == "":
        return len(s2)

    if s2 == "":
        return len(s1)

    if s1[-1] == s2[-1]:
        cost = 0
    else:
        cost = 1

    return min(
        [
            levenshtein_distance(s1[:-1], s2) + 1,
            levenshtein_distance(s1, s2[:-1]) + 1,
            levenshtein_distance(s1[:-1], s2[:-1]) + cost,
        ]
    )


def main():

    if DEBUG:
        sys.stdin = open("samples/01_input.txt")

    wish = input().lower()
    input()  # blank line

    words = []
    scores = []
    for _ in range(3):
        word = input()
        words.append(word)
        scores.append(levenshtein_distance(wish, word.lower()))

    print(words[scores.index(min(scores))])


if __name__ == "__main__":
    main()
