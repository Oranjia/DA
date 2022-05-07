"""
demo08_interp1d.py  插值
"""
import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as mp

# 造一组散点
min_val = -50
max_val = 50
x = np.linspace(min_val, max_val, 15)
y = np.sinc(x)

# 通过这一组散点，构建插值器函数(连续函数)
linear = si.interp1d(x, y, kind='cubic')

# 绘制插值器函数图像
mp.grid(linestyle=':')
mp.scatter(x, y, color='dodgerblue', label='samples')
px = np.linspace(min_val, max_val, 1000)
py = linear(px)
mp.plot(px, py)
mp.legend()
mp.show()
