"""
demo04_poly.py  测试多项式函数相关API
y = 4x<sup>3</sup> + 3x<sup>2</sup> - 1000x + 1
"""
import numpy as np
import matplotlib.pyplot as mp

P = [4, 3, -1000, 1]

# 画出函数图像
x = np.linspace(-20, 20, 1000)
y = np.polyval(P, x)
mp.grid(linestyle=':')
mp.plot(x, y)

# 画出驻点
Q = np.polyder(P)
xs = np.roots(Q)
print(xs)
ys = np.polyval(P, xs)
mp.scatter(xs, ys, s=100, marker='*',
	color='red', zorder=3)
mp.show()

