"""
demo01_fill.py   填充
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(0, 8*np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x/2) / 2 
# 绘制填充
mp.figure('Fill', facecolor='lightgray')
mp.title('Fill', fontsize=18)
mp.grid(linestyle=':')
mp.plot(x, sinx, color='dodgerblue', 
	label=r'$y=sin(x)$')
mp.plot(x, cosx, color='orangered',
	label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')
# 填充图像
mp.fill_between(x, sinx, cosx, sinx>cosx,
	color='dodgerblue', alpha=0.2)
mp.fill_between(x, sinx, cosx, sinx<cosx,
	color='orangered', alpha=0.2)

mp.legend()
mp.show()