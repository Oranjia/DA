"""
demo06_func.py   常用函数
"""
import numpy as np

# 数组裁剪 clip
ary = np.arange(1, 10)
print(ary)
print(ary.clip(min=3, max=8))

# 数组压缩 compress
r = ary.compress( 
	np.all([ary%2==0, ary%3==0], axis=0) )
print(r)

