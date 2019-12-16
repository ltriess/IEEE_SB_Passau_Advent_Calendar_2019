#!/usr/bin/env python3

import datetime
import sys

DEBUG = False

sleep = {
    0: [("20:00", "01:00"), ("01:30", "06:45"), ("08:00", "14:00"), ("14:45", "19:15")],
    2: [("19:00", "07:00"), ("12:00", "13:00")],
    7: [("20:00", "06:30")],
    11: [("22:00", "06:00")],
    18: [("00:00", "07:00")],
    31: [("23:00", "07:00")],
    51: [("22:00", "06:00")],
    66: [("21:00", "06:00"), ("13:00", "14:00")],
}


def str2time(time: str) -> (int, int):
    h, m = map(int, time.split(":"))
    return h, m


def get_age_descriptor(age: int) -> list:
    sk = list(sleep.keys()) + [123]
    for k in range(len(sk)):
        if sk[k] <= age < sk[k + 1]:
            return sleep[sk[k]]


def check_if_time_in_range(time: str, trange: tuple):
    time = datetime.time(*str2time(time))
    start = datetime.time(*str2time(trange[0]))
    end = datetime.time(*str2time(trange[1]))

    if start <= end:
        return start <= time <= end
    else:
        return start <= time or time <= end


def is_awake(time: str, age: int) -> (bool, bool):
    d = [check_if_time_in_range(time, r) for r in get_age_descriptor(age)]
    assert sum(d) <= 1
    awake = not any(d)
    return awake, awake and age < 2


def get_neighbors(house_num, residential_area):
    size = len(residential_area)
    pos = next(
        (
            (i, colour.index(house_num))
            for i, colour in enumerate(residential_area)
            if house_num in colour
        ),
        None,
    )
    if pos is None:
        raise ValueError("Cannot find house number")

    # return maximum of 8 neighbors (vertical, horizontal, and diagonal)
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = pos[0] + i
            y = pos[1] + j

            # do not include current house
            if i == 0 and j == 0:
                continue

            # stay within the grid of the residential area
            if x < 0 or y < 0:
                continue
            if x >= size or y >= size:
                continue

            neighbors.append(residential_area[x][y])

    return neighbors


def main():

    if DEBUG:
        sys.stdin = open("samples/24_input.txt")

    time = input()
    edge_length = int(input())
    residential_area = []
    for _ in range(edge_length):
        residential_area.append([int(x) for x in input().split(" ")])

    r = {}
    for _ in range(edge_length ** 2):
        descriptor = [int(x) for x in input().split(" ")]
        house_number = descriptor[0]

        total = len(descriptor[1:])
        awake = 0
        babies = 0
        for d in descriptor[1:]:
            a, s = is_awake(time, d)
            awake += int(a)
            babies += int(s)

        # there must be one other person be awake if a baby is awake
        if (babies > 0) and (awake == babies):
            awake += 1

        assert awake <= total

        r[house_number] = (awake, total)

    visited_house = int(input())
    neighbors = get_neighbors(visited_house, residential_area)

    prob = 0
    # increases by 10% for every awake person in the house
    prob += 10 * r[visited_house][0]
    # increases by 5% for every sleeping person in the house
    prob += 5 * (r[visited_house][1] - r[visited_house][0])
    # increases by 5% for every awake person in a neighboring house
    prob += 5 * sum(r[num][0] for num in neighbors)
    # increases by additional 1% per person in the visited house
    prob += 1 * r[visited_house][1]

    print("{p}%".format(p=min(prob, 100)))


if __name__ == "__main__":
    main()
