"""
demo05_matrix.py 矩阵
"""
import numpy as np

ary = np.arange(1, 7).reshape(2, 3)
print(ary, type(ary))
m = np.matrix(ary, copy=True)
print(m, type(m))
m[0,0] = 99
print(ary)

m2 = np.mat(ary) # 与源数组共享数据
print(m2, '<-- np.mat()')

m3 = np.mat('1 2 3; 4 5 6')
print(m3, '<-- np.mat("")')

# 矩阵乘法
print('-' * 45)
m = np.mat('1 4 7; 4 9 2; 1 6 3')
print(m * m, '<- matrix *')
a = np.array(m)
print(a * a, '<- ndarray *')

# 矩阵求逆
print('-' * 45)
m = m[:2, :]
print(m)
print(m.I)
print(m * m.I)

# 解方程组 
A = np.mat('3 3.2; 3.5 3.6')
B = np.mat('118.4; 135.2')
print(np.linalg.lstsq(A, B)[0])
print(A.I * B)

# 斐波那契数列
F = np.mat('1 1; 1 0')
n = 39
print( (F**n)[0,0] )

print(F**0)


