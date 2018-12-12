#!/usr/bin/env python
# coding=utf-8
def power(x, n):
    s = 1
    w = 1
    for w in range(n):
        s = s * x 
        w = w + 1
    return s 
print('底数为:')
x = int(input())
print('幂为:')
n = int(input())
print('计算结果是:')
print(power(x, n))

