#!/usr/bin/env python
# coding=utf-8
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return 0
    else:
        return -x


print(my_abs(-99))
