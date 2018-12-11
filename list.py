#!/usr/bin/env python
# coding=utf-8
classmates = ['Michael', 'Bob', 'Tracy'] # 定义 classmates list
classmates.append('Adam') # 在末尾 加上 Adam
classmates.insert(1, 'Jack')# 在位置1 插入jack
classmates.pop() # pop 出栈
classmates[2]='Sarah' # 修改指定位置
print(classmates)
print('classmates') # 转义
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'object-c'], 'Go']
print(len(s))
print(len(L))
print(len(s[2])) # list 中的 list 长度
