"""
demo02_ndarray.py  ndarray数组
"""
import numpy as np

# np.array()
a1 = np.array([[1,2,3], [4,5,6]])
print(a1)
# np.arange()
a2 = np.arange(0, 10, 2)
print(a2)
# np.zeros()
a3 = np.zeros(10, dtype='float32')
print(a3)
# np.ones()
a4 = np.ones((2,3), dtype='int32')
print(a4)
# np.zeros_like()   np.ones_like()
# 构建一个结构与a1相同的全0数组
print(np.zeros_like(a1))
# 构建一个结构与a3相同的全1数组
print(np.ones_like(a3))



