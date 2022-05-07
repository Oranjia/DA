"""
demo10_bubble.py
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

#自定义一种可以存放在ndarray里的类型，用于保存一个球
n = 100
balls = np.zeros(n, dtype=[
	('position', 'f8', 2), 
	('size', 'f8', 1), 
	('growth', 'f8', 1), 
	('color', 'f8', 4)])
# 为balls初始化
balls['position']=np.random.uniform(0,1,(n,2))
# for ball in balls:
# 	print(ball)
balls['size']=np.random.uniform(70, 90, n)
balls['growth']=np.random.uniform(10, 20, n)
balls['color']=np.random.uniform(0, 1, (n, 4))
# 画图
mp.figure('Animation', facecolor='lightgray')
mp.title('Animation', fontsize=18)
sc = mp.scatter(balls['position'][:,0], 
	balls['position'][:,1], s=balls['size'],
	color=balls['color'])


def update(number):
	ind = number % n
	balls[ind]['size'] = \
		np.random.uniform(60, 80, 1)

	# 不断更新界面
	balls['size'] += balls['growth']
	sc.set_sizes(balls['size'])

# 执行动画
anim = ma.FuncAnimation(
	mp.gcf(), update, interval=30)

mp.show()




