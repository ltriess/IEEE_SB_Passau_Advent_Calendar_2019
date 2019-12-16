#!/usr/bin/env python3

import sys

DEBUG = False


class Branch(object):
    def __init__(self, name):
        self.name = name
        self.color = None
        self.neighbors = []

    def add_neighbor(self, neighbor):
        assert isinstance(neighbor, Branch)
        self.neighbors.append(neighbor)

    def set_color(self, color):
        isinstance(color, int)
        self.color = color


def main():

    if DEBUG:
        sys.stdin = open("samples/16_input.txt")

    num_colors = int(input())
    num_branches = int(input())

    connections = []
    for _ in range(num_branches):
        connections.append([int(i) for i in input().split(" ")])

    # initialize tree
    tree = [Branch(i) for i in range(num_branches)]

    # add neighbors
    for i in range(num_branches):
        for j in range(num_branches):
            if connections[i][j] == 1:
                tree[i].add_neighbor(tree[j])

    # set color of first branch
    tree[0].set_color(1)
    color_out = [1]

    # set colors of remaining branches
    for b in range(1, num_branches):
        # check neighbor colors
        nc = [n.color for n in tree[b].neighbors if n.color is not None]
        # find available colors
        vc = [i + 1 for i in range(num_colors) if i + 1 not in nc]

        if len(vc) == 0:
            print("NO SOLUTION!")
            exit(0)

        # TODO: choosing vc[0] can lead to NO SOLUTION even if it is possible
        # TODO: need to check all possible solutions here
        tree[b].set_color(vc[0])
        color_out.append(tree[b].color)

    print(" ".join(str(c) for c in color_out))


if __name__ == "__main__":
    main()
