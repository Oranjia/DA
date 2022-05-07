"""
demo04_fft.py  傅里叶变换
"""
import numpy as np
import matplotlib.pyplot as mp
import numpy.fft as nf

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y1 = 4*np.pi * np.sin(x)
y2 = 4/3*np.pi * np.sin(3*x)
y3 = 4/5*np.pi * np.sin(5*x)

# 叠加正弦函数，合成方波
y = np.zeros(x.size)
for i in range(1, 1000):
	y += 4/(2*i-1)*np.pi * np.sin((2*i-1)*x)

# 基于傅里叶变换，拆解y函数
complex_ary = nf.fft(y)
y_copy = nf.ifft(complex_ary)

mp.subplot(121)
mp.title('Time Domain', fontsize=16)
mp.grid(linestyle=':')
mp.plot(x, y1, label='y1',alpha=0.2)
mp.plot(x, y2, label='y2',alpha=0.2)
mp.plot(x, y3, label='y3',alpha=0.2)
mp.plot(x, y, label='y')
mp.plot(x, y_copy.real, linewidth=7, alpha=0.3,  
		label='y_copy')
mp.legend()

# 绘制频域图像
freqs = nf.fftfreq(len(y), x[1]-x[0]) # 频率数组
pows = np.abs(complex_ary) # 能量数组
mp.subplot(122)
mp.title('Frequency Domain', fontsize=16)
mp.grid(linestyle=':')
mp.plot(freqs[freqs>0], pows[freqs>0], 
	color='orangered', label='Freq')
mp.legend()
mp.show()
