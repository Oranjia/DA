"""
demo08_divide.py  除法与取整
"""
import numpy as np

a = np.array([20, 20, -20, -20])
b = np.array([3, -3, 6, -6])

r = a / b
r = np.divide(a, b)
print(r)

print(np.floor(r))
print(np.ceil(r))
print(np.trunc(r))
print(np.round(r))





