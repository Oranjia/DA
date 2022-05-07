"""
demo05_shape.py  维度操作
"""
import numpy as np

# 视图变维
a = np.arange(1, 7)
print(a, a.shape)
b = a.reshape(2, 3)
print(b, b.shape)
b[0, 0] = 999
print(a)
print(b)
# 
c = a.reshape(-1, 2)
print(c)
print(c.ravel())

# 复制变维  copy()
print('-' * 45)
d = c.flatten()
print(c)
print(d)

# 就地变维
print('-' * 45)
print(a)
a.shape = (3, 2)
print(a)
a.resize(2, 3)
print(a)







