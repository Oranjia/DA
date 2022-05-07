"""
demo03_attr.py  属性
"""
import numpy as np

# 数组维度操作: shape
ary = np.arange(1, 10)
print(ary, ary.shape)
ary.shape = (3, 3)
print(ary, ary.shape)

# 数组元素的数据类型
print(ary, ary.dtype)
# ary.dtype = 'float32'
# print(ary, ary.dtype)
ary = ary.astype('float32')
print(ary, ary.dtype)

# 数组的长度
print(ary, 'size:', ary.size, 'len:', len(ary))

# 数组的索引下标
print('ary[1]:   ', ary[1])
print('ary[1][2]:', ary[1][2])
print('ary[1, 2]:', ary[1, 2])
print('-' * 45)
ary = np.arange(1, 28)
ary.shape = (3, 3, 3)
print(ary)

for i in range(ary.shape[0]):
	for j in range(ary.shape[1]):
		for k in range(ary.shape[2]):
			print(ary[i, j, k], end=' ')
