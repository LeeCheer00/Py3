#!/usr/bin/env python
# coding=utf-8
PI = 4 #初始化π
print('The program below will count the PI\' value!')
for i in range (1, 101, 1):
    PI = PI*4*i*(i+1)/(2*i+1)/(2*i+1) # 写紧凑, 没写紧凑不管用
print('PI\' value is: %.7f' % PI)




