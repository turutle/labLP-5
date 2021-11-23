#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Индивидуальное задание №13: Найти сумму аргументов, расположенных после минимального аргумента

def after_min(*args):
    if args:
        ans = 0
        idx = args.index(min(args))
        for item in args:
            if args.index(item) > idx:
                ans += item
        return ans
    else:
        return None


if __name__ == "__main__":
    print(after_min())
    print(after_min(3, 7, 1, 6, 9))
    print(after_min(1, 5, 8, -1, 4, 3, 9))