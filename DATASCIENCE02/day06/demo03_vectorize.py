"""
demo03_vectorize.py
"""
import numpy as np
import math as m

def foo(x, y):
	return m.sqrt(x**2 + y**2)

x, y = 3, 4
print(foo(x, y))
x, y = np.array([3,4,5]), np.array([4,5,6])

# print(foo(x, y))
# 把foo函数矢量化处理, 返回矢量化函数foo_vec
foo_vec = np.vectorize(foo)
print(foo_vec(x, y))
print(np.vectorize(foo)(x, y))

print(np.frompyfunc(foo, 2, 1)(x, y))
