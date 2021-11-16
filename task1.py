#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometricMid(*args):
    if args:
        ans = 1
        for item in args:
            ans *= item
        return pow(ans, 1/len(args))
    else:
        return None


if __name__ == "__main__":
    print(geometricMid())
    print(geometricMid(3, 7, 1, 6, 9))
    print(geometricMid(1, 5, 8, 4, 3, 9))