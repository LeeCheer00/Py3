#!/usr/bin/env python
# coding=utf-8
s = 1
pi = 1
i = 1
w = 1
W = 1
while W >= 1e-6:
    s = -s

    W = 1/(2*i+1)
    w = W * s
    pi = pi+w
    i = i+1
PI=4*pi
print('The PI\'s value is: %.7f' % PI)


    
 
