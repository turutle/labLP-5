#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Индивидуальное задание №13: Найти сумму аргументов, расположенных после минимального аргумента

def afterMin(*args):
    if args:
        ans = 0
        a = min(args)
        for i in range(args.index(a) + 1, len(args)):
            ans += args[i]
        return ans
    else:
        return None


if __name__ == "__main__":
    print(afterMin())
    print(afterMin(3, 7, 1, 6, 9))
    print(afterMin(1, 5, 8, -1, 4, 3, 9))