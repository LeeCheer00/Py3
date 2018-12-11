#!/usr/bin/env python
# coding=utf-8
s = set([1,1,2,2,3,3])
print(s)
s.add(4)# add加元素到set中
print(s)
s.remove(3)
print(s)

s1 = set([1,2,3])
s2 = set([2,4,6])
print(s1 | s2) # 并集
print(s1 & s2) # 与运算
z = [1,2,3]
# print(s(z)) error: object is not callable


