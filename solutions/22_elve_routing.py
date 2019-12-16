#!/usr/bin/env python3

import sys

DEBUG = True


def valid_position(position, card):
    for p in position:
        if p < 0 or p >= len(card):
            return False

    # The route shall never move over empty spots on the map.
    if card[position[0]][position[1]] == ".":
        return False

    return True


def move_one_step(position, move):
    # U - up
    # D - down
    # L - left
    # R - right
    if move == "U":
        return position[0] + 1, position[1]
    elif move == "D":
        return position[0] - 1, position[1]
    elif move == "L":
        return position[0], position[1] - 1
    elif move == "R":
        return position[0], position[1] + 1


def is_route_valid(start_point, end_point, instructions, card):
    # A route is valid as long as the start and end point are both on a +.
    if not card[start_point[0]][start_point[1]] == "+":
        return False, None

    if not card[end_point[0]][end_point[1]] == "+":
        return False, None

    route = [start_point]

    current_pos = start_point
    for i in instructions:
        # move in the same direction until we hit + or an invalid position
        while True:
            current_pos = move_one_step(current_pos, i)
            route.append(current_pos)

            if not valid_position(current_pos, card):
                return False, None

            if card[current_pos[0]][current_pos[1]] == "+":
                break

    # check if the current position is equal to the end point
    if not current_pos == end_point:
        return False, None

    return True, route


def find_uncovered_roads(card, covered):

    # check all horizontal roads
    for r, l in zip(card, covered):
        if sum(l) == len(card):
            continue
        else:
            # TODO
            print(r, l)
            pass

    # check all vertical roads

    # sorting: (x1, y1) - (x2, y2) with x1 < x2 || x1 == x2 & y1 < y2.
    # For lines p1 - p2 and p1' - p2' the following applies: p1 < p1' || p1 == p1' & p2 < p2'
    # TODO
    return []


def main():

    if DEBUG:
        sys.stdin = open("samples/22_input.txt")

    size = int(input())  # 3 ≤ size ≤ 15

    # . A blank space on the map.
    # - A part of the road that goes from left to right.
    # | A part of the road that goes from top to bottom.
    # + An intersection, turn or dead end. Between two + there is always at least one street part.
    m = [None] * size
    for i in range(size):
        m[size - 1 - i] = list(input())

    routes = []
    covered = [
        [True if m[j][i] == "." else False for i in range(size)] for j in range(size)
    ]
    invalid_routes = []

    num_routes = int(input())  # 0 ≤ routes ⋚ 20
    for _ in range(num_routes):
        # [start point] instructions [end point]
        r = input().split(" ")
        start_point = (
            int(r[0].replace("(", "").replace(",", "")),
            int(r[1].replace(")", "")),
        )
        instructions = r[2]
        end_point = (
            int(r[3].replace("(", "").replace(",", "")),
            int(r[4].replace(")", "")),
        )

        valid, route = is_route_valid(start_point, end_point, instructions, m)
        if valid:
            routes.append(route)
            for r in route:
                covered[r[0]][r[1]] = True
        else:
            invalid_routes.append(" ".join(r))

    # Are all routes valid?
    if len(invalid_routes) == 0:
        print("OK")
    else:
        print(len(invalid_routes))
        for r in invalid_routes:
            print(r)

    # Are all roads covered with valid routes?
    if sum(sum(s) for s in covered) == size * size:
        print("OK")
    else:
        uncovered_roads = find_uncovered_roads(m, covered)
        for r in uncovered_roads:
            print("{0} - {1}".format(r[0], r[1]))

    # Are there any superfluous routes?
    print("OK")
    raise NotImplementedError("Need to find superfluous routes.")


if __name__ == "__main__":
    main()
