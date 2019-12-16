#!/usr/bin/env python3

import sys

DEBUG = False


def main():

    if DEBUG:
        sys.stdin = open("samples/13_input.txt")

    num_cuboids = int(input())

    vol = []
    cuboids = []
    for _ in range(num_cuboids):
        x1, y1, z1, x2, y2, z2 = map(int, input().split(" "))

        h = abs(x2 - x1)
        w = abs(y2 - y1)
        d = abs(z2 - z1)

        vol.append(h * w * d)
        cuboids.append((x1, y1, z1, x2, y2, z2))

    union = {}
    for i in range(num_cuboids):
        for j in range(num_cuboids):
            if i == j:
                continue

            v = (
                max(
                    min(cuboids[i][3], cuboids[j][3])
                    - max(cuboids[i][0], cuboids[j][0]),
                    0,
                )
                * max(
                    min(cuboids[i][4], cuboids[j][4])
                    - max(cuboids[i][1], cuboids[j][1]),
                    0,
                )
                * max(
                    min(cuboids[i][5], cuboids[j][5])
                    - max(cuboids[i][2], cuboids[j][2]),
                    0,
                )
            )

            assert union.get(tuple(sorted((i, j))), v) == v
            union[tuple(sorted((i, j)))] = v

    vol = sum(vol) - sum(union.values())
    print(vol)


if __name__ == "__main__":
    main()
