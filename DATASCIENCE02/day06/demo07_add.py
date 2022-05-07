"""
demo07_add.py  通用函数
"""
import numpy as np

a = np.arange(1, 6)
print(a)
print(np.add(a, a))
print(np.add.reduce(a))
print(np.add.accumulate(a))
print(np.prod(a))
print(np.cumprod(a))

# 外和 与 外积
print(np.add.outer([10, 20, 30], a))
print(np.outer([10, 20, 30], a))

