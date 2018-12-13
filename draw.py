"""
=============================================================
Demo of the histogram (hist) function with multiple data sets
=============================================================

Plot histogram with multiple sample sets and demonstrate:

    * Use of legend with multiple sample sets
    * Stacked bars
    * Step curve with no fill
    * Data sets of different sample sizes

Selecting different bin counts and sizes can significantly affect the
shape of a histogram. The Astropy docs have a great section on how to
select these parameters:
http://docs.astropy.org/en/stable/visualization/histogram.html
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

n_bins =  5
x = np.random.randn(2000, 7)
#x= [[60.92, 61.12, 61.32, 67.74, 67.74],
#    [67.30, 67.27, 67.27, 69.09, 74.54],
#    [49.5, 49.41, 49.41, 49.61, 56.25],
#    [88.7, 88.69, 88.69, 89.02, 95.56],
#    [65.2, 65.07, 65.23, 65.56, 65.57],
#    [83.2, 82.83, 83.08, 83.59, 89.65],
#    [69.2, 69.08, 69.24, 69.73, 75.85],
#]
#x = x * 0.01
#print(x)

# x = ['happy', 'sad', 'digust', 'nerual', 'fear', 'surpise', 'angry']
# x = ['2']

#fig, axes = plt.subplots(nrows=2, ncols=2)
#ax0, ax1, ax2, ax3 = axes.flatten()
#ax0 =  axes.flatten()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

labels = ['Angry', 'Disgust', 'Fear', 'Happy'  ,'Sad','Surpise']
colors = ['red', 'tan', 'lime', 'black','blue', 'green', 'grey']
ax.hist(x, n_bins, density=False, histtype='bar', align='left', color=colors, label=labels) # hist()详细, 颜色, 标签
ax.legend(prop={'size': 10}) # 图例大小
ax.set_xticks(np.arange(-3.8, 3, 1.58))#　步长（起点，终点，　步长，　TYPE)
#ax.set_xticks(np.arange(-3.8, 80, 1.58))#　步长（起点，终点，　步长，　TYPE)
M_labels=['ReLu', 'L-ReLu', 'P-ReLu', 'Swish', 'Swish+']
ax.set_xticklabels(M_labels)
#ax.xticks(np.arrange(5)+1,M_labels)
ax.set_title('Accuracy with different activation function')
ax.set_xlabel('Method')
ax.set_ylabel('Accuracy')

#plot
plt.plot()
#ax1.hist(x, n_bins, density=True, histtype='bar', stacked=True)
#ax1.set_title('stacked bar')
#
#ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
#ax2.set_title('stack step (unfilled)')
#
## Make a multiple-histogram of data-sets with different length.
#x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
#ax3.hist(x_multi, n_bins, histtype='bar')
#ax3.set_title('different sample sizes')
#
# fig.tight_layout()

plt.show()
