"""
demo01_plot.py 基本绘图
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([45,81,36,51,19,92,23,51])
mp.plot(x, y)

# 绘制水平线
mp.hlines(60, 1, 6.5)
# 绘制垂直线
mp.vlines([1,2,3,4,5], 
		  [10,20,30,40,50], [25,35,45,55,65])
mp.show()

