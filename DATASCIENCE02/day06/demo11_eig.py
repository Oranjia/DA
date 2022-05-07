"""
demo11_eig.py  特征值与特征向量
"""
import numpy as np

A = np.mat('1 3 6; 4 8 9; 5 7 9')
print(A)
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)

# 逆向生成原始矩阵
eigvals[2:] = 0
A_ = eigvecs * np.diag(eigvals) * eigvecs.I
print(A_)

