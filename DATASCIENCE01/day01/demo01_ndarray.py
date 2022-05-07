"""
demo01_ndarray.py   多维数组
"""
import numpy as np

ary = np.array([1,2,3,4,5,6])
print(ary, type(ary))

# ndarray的运算
ary = ary + 10
print(ary)
ary = ary * 2
print(ary)
ary = ary + ary
print(ary)
ary = ary > 50 
print(ary)

