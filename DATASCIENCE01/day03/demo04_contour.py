"""
demo04_contour.py 等高线图
"""
import numpy as np
import matplotlib.pyplot as mp

n = 500
x, y = np.meshgrid(np.linspace(-3, 3, n), 
				   np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

# 绘制等高线图
mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=18)
mp.grid(linestyle=':')
cntr = mp.contour(x, y, z, 8, colors='black',
	linewidths=0.5)
# 为等高线图添加高度标签
mp.clabel(cntr, inline_spacing=2, fmt='%.1f',
          fontsize=10)
mp.contourf(x, y, z, 8, cmap='jet')
mp.show()

