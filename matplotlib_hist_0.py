#!/usr/bin/env python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np


# 创建一个点数为 8 * 6 的窗口, 并设置分辨率为 100像素/每英寸
plt.figure(figsize=(8, 6), dpi = 100)


# 再创建一个规格为 1 * 1 的子图
plt.subplot(1, 1, 1)


# 柱子有几堆
N = 7


# 包含每个柱子的对应值和序列
values = (61.1, 67.3, 49.5, 88.7, 65.2, 83.2, 69.2) #{} 会导致这被看作是集合,不是list,无序

# 包含每个柱子下标的序列
index = np.arange(N)


# 柱子的宽度
width = 0.35

# 绘制柱状图, 每根柱子的颜色为紫罗兰色
p2 = plt.bar(index, values, width, label="ReLu", color="#87CEFA")


# 设置横轴标签
plt.xlabel('Methods')
# 设置纵轴标签
plt.ylabel('Accuracy (%)')

# 添加标题
plt.title('Accuracy on different Emtoions')


# 横轴标签类目
classes = ('Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral')
# 添加纵横轴的刻度
plt.xticks(index, classes)


# 添加图例
plt.legend(loc="upper right")


plt.show()
