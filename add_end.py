#!/usr/bin/env python
# coding=utf-8
def add_end(L=None):
    if L is None: # 'END' 'END' 'END'
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())
