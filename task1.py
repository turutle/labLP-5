#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometricMid(*args):
    if args:
        ans = 1
        a = 0
        for item in args:
            ans *= item
            a += 1
        return pow(ans, 1/a)
    else:
        return None


if __name__ == "__main__":
    print(geometricMid())
    print(geometricMid(3, 7, 1, 6, 9))
    print(geometricMid(1, 5, 8, 4, 3, 9))