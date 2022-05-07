"""
demo02_svd.py 奇异值分解
"""
import numpy as np

m = np.mat('4 11 14; 8 7 -2')
print(m)
U, sv, V = np.linalg.svd(m, full_matrices=False)
print(U)
print(U * U.I, '<- U')
print(V)
print(V * V.I, '<- V')
print(sv)

# 通过U x S x V计算原矩阵
sv[1] = 0
print(U * np.diag(sv) * V)


