#!/usr/bin/env python3

import math
import sys

DEBUG = False

g = 9.807  # gravitational constant [m/s^2]
h_wall = 5  # in meters
fov_down = -15  # degrees
fov_up = 60  # degrees
fov_steps = 1  # degrees
num_levels = 10
hit_radius = 0.5  # meters around the target


def get_range(initial_velocity, fire_angle, height_above_ground):
    fire_angle = math.radians(fire_angle)

    v_0x = initial_velocity * math.cos(fire_angle)  # initial velocity in x
    v_0y = initial_velocity * math.sin(fire_angle)  # initial velocity in y

    return (
        -(v_0x / g) * (-v_0y + math.sqrt((v_0y ** 2) - (2 * g * -height_above_ground))),
        -(v_0x / g) * (-v_0y - math.sqrt((v_0y ** 2) - (2 * g * -height_above_ground))),
    )


def get_firepower(level):
    # velocity in meters / second
    return 10 * level


def main():

    # TODO 4 of 7 test cases fail

    if DEBUG:
        sys.stdin = open("samples/18_input.txt")

    num_obstacles = int(input())
    obstacles = []
    for _ in range(num_obstacles):
        obstacles.append(tuple(int(i) for i in input().split(" ")))
    d_target = int(input())

    # compute all possible configurations for angle and firepower to hit the target
    possibilities = []
    for angle in range(fov_down, fov_up + 1, fov_steps):
        for level in range(1, num_levels + 1):
            v_0 = get_firepower(level)  # initial velocity
            d_hitpoint_ground = get_range(v_0, angle, h_wall)

            if (
                d_target - hit_radius <= d_hitpoint_ground[0] <= d_target + hit_radius
                or d_target - hit_radius
                <= d_hitpoint_ground[1]
                <= d_target + hit_radius
            ):
                possibilities.append((level, angle))

    # sort according to firepower and angle
    possibilities = sorted(possibilities)

    # there is no way to hit the target
    if len(possibilities) < 1:
        print("IMPOSSIBLE")
        return

    # there are no obstacles, therefore output the lowest possible firepower and angle
    if len(obstacles) < 1:
        print(possibilities[0][1], possibilities[0][0])
        return

    # check collisions for all possibilities on all obstacles
    for p in possibilities:
        level, angle = p
        hit = []
        for o in obstacles:
            height, d_o = o
            d_h = get_range(get_firepower(level), angle, h_wall - height)

            if (
                d_o - hit_radius <= d_h[0] <= d_o + hit_radius
                or d_o - hit_radius <= d_h[1] <= d_o + hit_radius
            ):
                hit.append(True)
            else:
                hit.append(False)

        if not any(hit):
            print(p[1], p[0])
            return

    print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
