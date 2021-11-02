#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonMid(*args):
    if args:
        a = ans = 0
        for item in args:
            a += 1
            ans += 1/item
        return a/(ans)
    else:
        return None

if __name__ == "__main__":
    print(harmonMid())
    print(harmonMid(3, 7, 1, 6, 9))
    print(harmonMid(1, 5, 8, 4, 3, 9))