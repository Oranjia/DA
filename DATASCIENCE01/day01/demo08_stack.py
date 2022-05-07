"""
demo08_stack.py 组合与拆分
"""
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
print(a, '<- a')
print(b, '<- b')
# 水平方向操作
c = np.hstack((a, b))
print(c, '<- c')
a, b = np.hsplit(c, 2)
print(a, '<- a')
print(b, '<- b')

# 垂直方向操作
c = np.vstack((a, b))
print(c, '<- c')
a, b = np.vsplit(c, 2)
print(a, '<- a')
print(b, '<- b')

# 深度方向操作
c = np.dstack((a, b))
print(c, '<- c')
a, b = np.dsplit(c, 2)
print(a, '<- a')
print(b, '<- b')

# 简单一维数组的组合方案
# 一组x坐标    和     一组y坐标
x = np.array([4.6, 1.9, 8.4, 9.3, 4.6, 1.0, 1.3])
y = np.array([4.7, 5.3, 8.4, 9.1, 0.4, 5.6, 1.0])
# 变两行
points = np.row_stack((x, y))
print(points)
# 变两列
points = np.column_stack((x, y))
print(points)
# 通过points(7*2) 拆出x与y坐标数组
x, y = np.hsplit(points, 2)
print(x)
print(y)
x, y = points[:,0], points[:,1]
print(x)
print(y)







