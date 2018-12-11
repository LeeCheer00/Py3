#!/usr/bin/env python
# coding=utf-8
name = input('请输入您的名字:')
s1 = int(input("请输入您的第一次成绩:"))
s2 = int(input("请输入您的第二次成绩:"))
s3 = 0
s4 = 0
s5 = 0
if s2 >= s1:
    s4 = s2 - s1
    s3 = "提升"
    s5 = s4 / s1 * 100

else:
    s4 = s1 - s2
    s3 = "降低"
    s5 = s4 / s1 * 100


print("Hello, %s, 你的成绩%s了%s分,%s了%.1f%%" % (name,s3,s4,s3,s5))
