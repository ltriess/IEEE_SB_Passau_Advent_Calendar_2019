#!/usr/bin/env python3

import math
import sys

DEBUG = False


class Circle(object):
    def __init__(self, x, y, db):
        self.x = int(x)
        self.y = int(y)

        # at 2m there is an intensity of 100dB
        # |I2 - I1| = 20 * log(D2 / D1) with I1 = 100 and D1 = 2
        # want to find D2 with I2 = db
        self.r = 10 ** (1 / 20 * abs(float(db) - 100) + math.log10(2))


def circle_intersection(circle1, circle2):

    x1, y1, r1 = circle1.x, circle1.y, circle1.r
    x2, y2, r2 = circle2.x, circle2.y, circle2.r

    dx, dy = x2 - x1, y2 - y1
    d = math.sqrt(dx * dx + dy * dy)
    if d > r1 + r2:
        return None  # no solutions, the circles are separate
    if d < abs(r1 - r2):
        return None  # no solutions because one circle is contained within the other
    if d == 0 and r1 == r2:
        return (
            None  # circles are coincident and there are an infinite number of solutions
        )

    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h = math.sqrt(r1 * r1 - a * a)
    xm = x1 + a * dx / d
    ym = y1 + a * dy / d

    xs1 = round(xm + h * dy / d)
    xs2 = round(xm - h * dy / d)
    ys1 = round(ym - h * dx / d)
    ys2 = round(ym + h * dx / d)

    return (xs1, ys1), (xs2, ys2)


def main():

    if DEBUG:
        sys.stdin = open("samples/15_input.txt")

    a = Circle(*input().split(" "))
    b = Circle(*input().split(" "))
    c = Circle(*input().split(" "))

    i_ab = circle_intersection(a, b)
    i_ac = circle_intersection(a, c)
    i_bc = circle_intersection(b, c)

    # check valid intersection
    if i_ab[0] in i_ac:
        pos = i_ab[0]
    elif i_ab[1] in i_ac:
        pos = i_ac[1]
    else:
        raise ValueError

    if pos not in i_bc:
        raise ValueError

    print("Present at {p}".format(p=pos))


if __name__ == "__main__":
    main()
