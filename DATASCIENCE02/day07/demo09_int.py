"""
demo09_int.py  积分
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as mc

def f(x):
	return 2 * x**2 + 3*x + 4

a, b = -5, 5
x = np.linspace(a, b, 500)
y = f(x)

# 使用微元法求积分
n = 50
px = np.linspace(a, b, n+1)
py = f(px)
area = 0
for i in range(n):
	area += (py[i+1] + py[i]) * (px[1]-px[0]) / 2
print(area)

# 使用scipy提供的函数计算定积分
import scipy.integrate as si
area = si.quad(f, a, b)[0]
print(area)

mp.grid(linestyle=':')
mp.plot(x, y, color='dodgerblue', linewidth=5)
for i in range(n):
    mp.gca().add_patch(mc.Polygon([
        [px[i], 0], [px[i], py[i]],
        [px[i + 1], py[i + 1]], [px[i + 1], 0]],
        fc='deepskyblue', ec='dodgerblue',
        alpha=0.5))
mp.show()

