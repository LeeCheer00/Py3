#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple


# 7种表情
n_groups = 7

values = [[61.1, 67.3, 49.5, 88.7, 65.2, 83.2, 69.2], #{} 会导致这被看作是集合,不是list,无序
          [60.92, 67.27, 49.41, 88.69, 65.07, 82.83, 69.08],
          [61.12, 67.27, 49.41, 88.69, 65.23, 83.08, 69.24],
          [61.32, 69.09, 49.61, 89.02, 65.56, 83.59, 69.73], 
          [67.74, 74.54, 56.25, 95.57, 71.85, 89.9, 75.85]
          ]

#print(values[0])


fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.1
classes = ('Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral')
labels = ('ReLu', 'P-ReLu', 'L-ReLu', 'Swish', 'Swish+')
colors = ('Red', 'Blue', 'Yellow', 'green', 'tan')
for x in range(5):
#print(labels[0])
    rects = ax.bar(index+x*bar_width, values[x], bar_width, color = colors[x])
#rects2 = ax.bar(index+bar_width, values[1], bar_width, color = colors[1]) 
#rects3 = ax.bar(index+2*bar_width, values[2], bar_width, color = colors[2])
#rects4 = ax.bar(index+3*bar_width, values[3], bar_width, color = colors[3])
#rects5 = ax.bar(index+4*bar_width, values[4], bar_width, color = colors[4])



ax.set_xlabel('Emotions')
ax.set_ylabel('Accuracy(%)')
ax.set_title('Accuracy on different Emotions')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(classes)
ax.legend(labels, prop = {'size':10}, loc = 2)

fig.tight_layout()
plt.show()
