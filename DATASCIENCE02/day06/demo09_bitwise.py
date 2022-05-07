"""
demo09_bitwise.py  二进制
"""
import numpy as np

a = np.array([2,-3,-9,6,-1,2])
b = np.array([3, 4, 6,2, 3,4])
print(a^b<0)


a = np.arange(210000)
print(a[a & (a-1) == 0])