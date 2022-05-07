"""
demo06_random.py 
"""
import numpy as np

# 得到一组随机数，每个元素表示： 
# 命中率0.3  投10个进几个？
r = np.random.binomial(10, 0.3, 100000)
for i in range(11):
	print(i, ' ->', (r==i).sum() / 100000 )

# 客服案例
r = np.random.binomial(3, 0.6, 100000)
print((r==0).sum() / 100000 )


# 超几何分布
r = np.random.hypergeometric(7, 3, 3, 200000)
for i in range(4):
	print(i, ' ->', (r==i).sum() / 200000 )
