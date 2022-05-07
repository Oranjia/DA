"""
demo10_sin.py  合成方波
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y1 = 4*np.pi * np.sin(x)
y2 = 4/3*np.pi * np.sin(3*x)
y3 = 4/5*np.pi * np.sin(5*x)

# 叠加正弦函数，合成方波
y = np.zeros(x.size)
for i in range(1, 1000):
	y += 4/(2*i-1)*np.pi * np.sin((2*i-1)*x)

mp.grid(linestyle=':')
mp.plot(x, y1, label='y1',alpha=0.2)
mp.plot(x, y2, label='y2',alpha=0.2)
mp.plot(x, y3, label='y3',alpha=0.2)
mp.plot(x, y, label='y')
mp.legend()
mp.show()
