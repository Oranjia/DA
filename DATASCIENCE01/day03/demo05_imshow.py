"""
demo05_imshow.py  热成像图
"""
import numpy as np
import matplotlib.pyplot as mp

n = 500
x, y = np.meshgrid(np.linspace(-3, 3, n), 
				   np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

# 绘制等高线图
mp.figure('Imshow', facecolor='lightgray')
mp.title('Imshow', fontsize=18)
mp.grid(linestyle=':')
# mp.imshow(z, cmap='jet', origin='lower')
mp.imshow(z, cmap='gist_rainbow', origin='lower')
# mp.imshow(z, cmap='gray', origin='lower')
mp.show()

