"""
demo08_gridline.py  刻度网格线
"""
import matplotlib.pyplot as mp

y = [1, 10, 100, 1000, 100, 10, 1]
# 设置刻度定位器
mp.figure('Grid Line', facecolor='lightgray')

mp.subplot(211)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
# 刻度网格线
ax.grid(which='major', axis='both', 
		color='orangered', linewidth=0.5)
ax.grid(which='minor', axis='both', 
		color='orangered', linewidth=0.25)
mp.plot(y, 'o-')

mp.subplot(212)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
# 刻度网格线
ax.grid(which='major', axis='both', 
		color='orangered', linewidth=0.5)
ax.grid(which='minor', axis='both', 
		color='orangered', linewidth=0.25)
mp.semilogy(y, 'o-')


mp.show()
