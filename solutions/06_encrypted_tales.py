#!/usr/bin/env python3

import sys

DEBUG = True

val = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
frequency = "etaoinshrdlcumwfgypbvkjxqz"

assert len(frequency) == len(val) // 2


def check_password(ciphertext, password, excludes):
    # Plaintext + Password = Ciphertext

    plaintext = ""
    for i, t in enumerate(ciphertext):
        # skip special characters
        if t not in val:
            plaintext += t
        else:
            current = val.index(t)
            shift = current - val.index(password[i % len(password)])
            new = current - shift

            plaintext += val[-new] if new < 0 else val[new]

    if plaintext[0].islower():
        excludes[0].append(password[0])
        return False, excludes

    for i in range(len(plaintext) - 2):
        if (
            plaintext[i] == "."
            and plaintext[i + 1] == " "
            and plaintext[i + 2].islower()
        ):
            pwd_idx = (i + 2) % len(password)
            excludes[pwd_idx].append(password[pwd_idx])
            return False, excludes

    f = [sum(x == c for x in plaintext.lower()) for c in frequency]
    if f == sorted(f)[::-1]:
        return True, excludes
    else:
        return False, excludes


def increment(lst, add=0):
    if lst[add] == len(val) // 2 - 1:  # exclude all lower case
        lst[add] = 0
        increment(lst, add + 1)
    else:
        lst[add] += 1

    return lst


def main():

    if DEBUG:
        sys.stdin = open("samples/06_input.txt")

    pw_length = int(input())
    password = ["A"] * pw_length

    ciphertext = ""
    while True:
        try:
            inp = input()
            if len(inp) == 0:
                ciphertext += " "
            else:
                ciphertext += inp
        except EOFError:
            break

    rotate = [0] * pw_length
    excludes = [[]] * pw_length
    while not "".join(password) == "".join([val[len(val) // 2]] * pw_length):
        # directly jump to next if exclude case
        if any(password[i] in excludes[i] for i in range(pw_length)):
            rotate = increment(rotate)
            password = [val[r] for r in rotate]

        check, excludes = check_password(ciphertext, "".join(password), excludes)

        if check:
            print("FOUND:", "".join(password))

        rotate = increment(rotate)
        password = [val[r] for r in rotate]

    raise NotImplementedError("So far most stupid solution...")


if __name__ == "__main__":
    main()
