"""
demo09_scatter.py 散点图
"""
import numpy as np
import matplotlib.pyplot as mp

n = 200
x = np.random.normal(175, 7, n)
y = np.random.normal(65, 10, n)
mp.figure('Scatter', facecolor='lightgray')
mp.title('Scatter', fontsize=18)
mp.grid(linestyle=':')

d = (x-175)**2 + (y-65)**2
mp.scatter(x, y, marker='o', s=70,
	c=d, cmap='gist_rainbow', label='Samples')
mp.legend()
mp.show()
