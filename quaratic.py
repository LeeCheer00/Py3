#!/usr/bin/env python
# coding=utf-8
import math
def quadratic(a, b, c): 
    if a == 0:
        if b != 0:
            x = -c/b
            return x, x
        else:
            if c == 0:
                print('0=0')
            else:
                print('c != 0') 
    else:
        if b*b - 4*a*c < 0:
            print('There is no answer!')
        else:
            nx = ((-b + math.sqrt(b*b-4*a*c)))/(2*a)
            ny = ((-b - math.sqrt(b*b-4*a*c)))/(2*a)
            return nx, ny

#    
#print('quadratic(2, 3, 1)=', quadratic(2, 3, 1))
#print('quadratic(1, 3, -4)=', quadratic(1, 3, -4))
#
#
#if quadratic(2, 3, 1) != (-0.5, -1.0):
#    print('测试失败')
#elif quadratic(2, 3, 1) != (-0.5, -1.0):
#    print('测试失败')
#else:
#    print('测试成功')

print(quadratic(2,3,1))
