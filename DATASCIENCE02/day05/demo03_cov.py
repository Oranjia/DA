"""
demo03_cov.py  协方差
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt

def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	t = time.strftime('%Y-%m-%d')
	return t

dates, vale_closing_prices = \
	np.loadtxt('../da_data/vale.csv', 
		delimiter=',', usecols=(1, 6),
		unpack=True, dtype='M8[D], f8',
		converters={1:dmy2ymd})

bhp_closing_prices = np.loadtxt(
	'../da_data/bhp.csv', delimiter=',',
	usecols=(6,))

# 计算协方差
vale_mean = np.mean(vale_closing_prices)
bhp_mean = np.mean(bhp_closing_prices)
vale_dev = vale_closing_prices - vale_mean 
bhp_dev = bhp_closing_prices - bhp_mean
cov = np.mean(vale_dev * bhp_dev)
print(cov)

# 相关系数
coef = cov / (bhp_closing_prices.std() *\
 vale_closing_prices.std())
print(coef)

# 相关矩阵
m = np.corrcoef(bhp_closing_prices, vale_closing_prices,)
print(m, m[0,1])

v = np.cov(bhp_closing_prices, vale_closing_prices)
print(v)





