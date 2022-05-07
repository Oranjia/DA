"""
demo07_surface.py 三维曲面图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 500
x, y = np.meshgrid(np.linspace(-3, 3, n), 
				   np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

# 绘制等高线图
mp.figure('3D Surface', facecolor='lightgray')
mp.title('3D Surface', fontsize=18)
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
ax3d.plot_surface(x, y, z, rstride=30,
	cstride=30, cmap='jet')
mp.tight_layout()
mp.show()

