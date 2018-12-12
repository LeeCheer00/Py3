#!/usr/bin/env python
# coding=utf-8
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny



print(move(2,2,4,0)) # it's tuple
