#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoid(x):
    a = []
    for item in x:
        a.append(1 /(1 + math.exp(-item)))
    return a 



x = np.arange(-5., 4., 0.05)

sig = sigmoid(x)
swi = sig * x 
plt.plot(x, swi)

############################################################# plt.gca()是ax 继承前面画出来的头像
ax = plt.gca() # 以下代码为把(0,0)放到坐标轴上
ax.spines['right'].set_color('none') # 去除上\右边的坐标线
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0)) # 下轴移到0
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0)) # 左轴移到0
ax.set_title('Swish activation function') # 名称
ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))#设置x主坐标间隔 1
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))#设置x从坐标间隔 0.1
ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))#设置y主坐标间隔 1
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))#设置y从坐标间隔 0.1
ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')#由每个x主坐标出发对x主坐标画垂直于x轴的线段
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')#由每个x主坐标出发对x主坐标画垂直于x轴的线段
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
plt.show()
