#!/usr/bin/env python3

import sys

DEBUG = False


def main():

    if DEBUG:
        sys.stdin = open("samples/19_input.txt")

    m, n = map(int, input().split(" "))

    edges = []
    nodes = []
    for _ in range(n):
        s1, s2 = map(int, input().split("->"))

        # check in which components the statements occur, must be 0 or 1 times
        idx1 = [i for i, n in enumerate(nodes) if s1 in n]
        idx2 = [i for i, n in enumerate(nodes) if s2 in n]

        assert 0 <= len(idx1) <= 1
        assert 0 <= len(idx2) <= 1

        idx1 = idx1[0] if len(idx1) > 0 else None
        idx2 = idx2[0] if len(idx2) > 0 else None

        if idx1 is None and idx2 is None:
            # both nodes did not occur yet, this makes a new component
            edges.append([tuple(sorted((s1, s2)))])
            nodes.append([s1, s2])
        elif (
            (idx1 is None and idx2 is not None)
            or (idx1 is not None and idx2 is None)
            or (idx1 == idx2)
        ):
            # one of the nodes already exists and the other is new
            # or both of the nodes appear in the same component
            p = idx1 if idx1 is not None else idx2  # index of component

            edges[p].append(tuple(sorted((s1, s2))))
            nodes[p].append(s1)
            nodes[p].append(s2)
        elif idx1 is not None and idx2 is not None and not idx1 == idx2:
            # both nodes occurred, but in different components, they are now connected
            edges[idx1] += edges[idx2] + [tuple(sorted((s1, s2)))]
            del edges[idx2]
            nodes[idx1] += nodes[idx2] + [s1, s2]
            del nodes[idx2]
        else:
            raise ValueError

    assert len(edges) == len(nodes)
    components = len(nodes)

    # flatten lists and count unique items
    edges = len({item for sublist in edges for item in sublist})
    nodes = len({item for sublist in nodes for item in sublist})

    # TODO: I am missing something, 3 of 10 test cases fail
    print(edges - nodes + 2 * components)


if __name__ == "__main__":
    main()
