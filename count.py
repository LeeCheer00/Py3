#!/usr/bin/env python
# coding=utf-8
def count(*nums):
    sum = 0
    for n in nums:
        sum = sum + n * n
    return sum



print(count(1,2,3,4))
