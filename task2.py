#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmon_mid(*args):
    if args:
        ans = 0
        if not(0.in(args)):
            for item in args:
                ans += 1/item
            return len(args) / ans
        else:
            return 0
    else:
        return None

if __name__ == "__main__":
    print(harmon_mid())
    print(harmon_mid(3, 7, 1, 6, 9))
    print(harmon_mid(1, 5, 8, 4, 3, 9))