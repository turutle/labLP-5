#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Индивидуальное задание: Найти сумму аргументов, у которых имя содержит четное количество символов

def after_min(**kwargs):
    if kwargs:
        ans = 0
        a = min(kwargs)
        for i in range(kwargs.index(a) + 1, len(kwargs)):
            ans += kwargs[i]
        return ans
    else:
        return None


if __name__ == "__main__":
    print(after_min())
    print(after_min(3, 7, 1, 6, 9))
    print(after_min(1, 5, 8, -1, 4, 3, 9))