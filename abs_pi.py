#!/usr/bin/env python
# coding=utf-8
s = 1
pi = 1
i = 1
w = 1
while abs(w) >= 1e-6: # abs() 绝对值运算
    s = -s

    w = s/(2*i+1)
    pi = pi+w
    i = i+1
PI=4*pi
print('The PI\'s value is: %.7f' % PI)


    
 
