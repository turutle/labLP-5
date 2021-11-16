#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Индивидуальное задание: Найти сумму аргументов, у которых имя содержит четное количество символов

def even_sum(**kwargs):
    if kwargs:
        ans = 0
        for name, values in kwargs.items():
            if len(name) % 2 == 0:
                ans += sum(values)
        return ans
    else:
        return None


if __name__ == "__main__":
    print(even_sum())
    print(even_sum(name = [10, 11, 0, 1], first = [1, 200, 4], notodd = [1, 20, 4, -10, 2]))