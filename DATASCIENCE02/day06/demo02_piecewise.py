"""
demo02_piecewise.py   数组处理函数
"""
import numpy as np

ary = np.array([32,-96,-21,35,-34,53,5])
sign_ary = np.sign(ary)
print(sign_ary)

# np.piecewise处理数组
ary = np.array([88, 70, 60, 50, 40])
r = np.piecewise(ary, [ary<60, ary>=60], [0, 1])
print(r)
