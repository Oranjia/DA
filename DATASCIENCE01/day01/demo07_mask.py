"""
demo07_mask.py  掩码操作
"""
import numpy as np
# bool掩码
a = np.arange(10)
mask = a % 2 == 0
print(a[mask])
print(a[a%2==0])
# 3与7的公倍数
a = np.arange(1, 100)
print(a[(a%3==0) & (a%7==0)])

# 索引掩码
a = np.array([10, 20, 30, 40])
mask = [0,3,2,0,1,2,0,3,1,2,3,0,2]
print(a[mask])

# 为商品排序
products = np.array(
	['Mi', 'Huawei', 'Apple', 'Sansung'])
prices = np.array([2999, 4999, 8888, 3999])
# 为数组排序，返回有序索引
indices = np.argsort(prices)
print(products[indices])


