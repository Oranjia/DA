"""
demo03_svd.py  奇异值分解
"""
import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as mp

# True: 读取灰度图  二维数组
image = sm.imread('../da_data/lily.jpg', True)
print(image.shape, image[0,0])

# 提取image的特征信息
image = np.mat(image)
eigvals, eigvecs = np.linalg.eig(image)
print(eigvals.shape, eigvecs.shape)
# 抹掉部分特征值
eigvals[50:] = 0
image2 = eigvecs * np.diag(eigvals) * eigvecs.I

# 奇异值分解
U, sv, V = np.linalg.svd(image)
sv[50:] = 0
image3 = U * np.diag(sv) * V

# 画图

mp.subplot(2,2,1)
mp.imshow(image, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(2,2,2)
print(image2.dtype)
mp.imshow(image2.real, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(2,2,4)
print(image3.dtype)
mp.imshow(image3.real, cmap='gray')
mp.xticks([])
mp.yticks([])
mp.tight_layout()


mp.show()


