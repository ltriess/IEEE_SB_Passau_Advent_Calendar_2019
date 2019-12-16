#!/usr/bin/env python3

import sys

DEBUG = True


def main():

    if DEBUG:
        sys.stdin = open("samples/04_input.txt")

    n = int(input())  # number of samples
    r = int(input())  # sample rate, r <= n
    f = int(input())  # frequency in Hz, 1 ≤ f ≤ r/2
    # factor by which the amplitude of the frequency is to be changed, 0 ≤ a ≤ 10
    a = int(input())
    # PCM samples, float64, mono, with values between -(2^15) ≤ x,y,z ≤ (2^15)-1
    pcm = [float(x) for x in input().split(" ")]

    print(n, r, f, a)
    print(pcm)

    raise NotImplementedError


if __name__ == "__main__":
    main()
