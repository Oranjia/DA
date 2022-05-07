"""
demo06_scatter.py  三维散点图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 300
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)

mp.figure('3D Scatter', facecolor='lightgray')
mp.title('3D Scatter', fontsize=18)
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
d = x**2 + y**2 + z**2
ax3d.scatter(x, y, z, s=80, c=d, cmap='jet')
mp.tight_layout()
mp.show()
