"""
demo02_plot.py  基本绘图
"""
import numpy as np
import matplotlib.pyplot as mp

#从-pi到pi拆1000个点
x = np.linspace(-np.pi, np.pi, 1000)
sinx = np.sin(x)
# 画一个y = cos(x)/2
cosx = np.cos(x) / 2

# 控制可视区间
# mp.xlim(0, np.pi)
# mp.ylim(0, 1)

# 修改x轴的刻度
vals = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
texts = [r'$-\pi$', r'$-\frac{\pi}{2}$', '0', 
		 r'$\frac{\pi}{2}$', r'$\pi$']
mp.xticks(vals, texts)

# 设置坐标轴
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
mp.yticks([-1.0, -0.5, 0.5, 1.0])

mp.plot(x, sinx, linestyle='-.', linewidth=2, 
	color='dodgerblue', alpha=0.8,
	label=r'$y = sin(x)$')
mp.plot(x, cosx, linestyle='--', linewidth=2,
	color='orangered', alpha=0.8, 
	label=r'$y = \frac{1}{2}cos(x)$')

# 绘制特殊点
mp.scatter([np.pi/2, np.pi/2], [1, 0],
	s=[120,80], marker='o', edgecolor='red', 
	facecolor='green', zorder=3)

# 为特殊点添加备注
mp.annotate(r'$[\frac{\pi}{2}, 1]$', 
	xycoords='data', xy=(np.pi/2, 1), 
	textcoords='offset points', xytext=(20, 30),
	fontsize=14, arrowprops=dict(
		arrowstyle='->',
		connectionstyle='angle3'))

mp.legend()
mp.show()

