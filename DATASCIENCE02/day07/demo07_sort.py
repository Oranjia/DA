"""
demo07_sort.py 排序
"""
import numpy as np

products = np.array(
	['MI', 'OPPO', 'VIVO', 'APPLE', 'HUAWEI'])
prices = np.array([2999,3999,3999,8888,4999])
volumes = np.array([60, 55, 65, 30, 90])
# 普通排序
print(np.msort(prices))
# 先按价格排序，再按销量倒序排序
indices = np.lexsort((-volumes, prices))
print(products[indices])

# 插入排序
A = np.array([1, 2, 3, 4, 7, 9])
B = np.array([5, 8])
indices = np.searchsorted(A, B)
print(indices)
C = np.insert(A, indices, B)
print(C)
