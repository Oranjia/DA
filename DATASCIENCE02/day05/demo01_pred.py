"""
demo01_pred.py  线性预测
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt

def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	t = time.strftime('%Y-%m-%d')
	return t

dates, opening_prices, highest_prices, \
	lowest_prices, closing_prices = \
	np.loadtxt('../da_data/aapl.csv', 
		delimiter=',', usecols=(1,3,4,5,6),
		unpack=True, dtype='M8[D],f8,f8,f8,f8',
		converters={1:dmy2ymd})

# 绘制收盘价折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.grid(linestyle=':')
# 设置刻度定位器
import matplotlib.dates as md
ax = mp.gca()
ax.xaxis.set_major_locator( # 每周一为主刻度
	md.WeekdayLocator(byweekday=md.MO))
# 每天一个次刻度
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置主刻度文本格式
ax.xaxis.set_major_formatter(
	md.DateFormatter('%Y/%m/%d'))
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, color='dodgerblue',
	label='Closing Price', linewidth=2,
	linestyle='--')

# 线性预测 
# 通过前6天的股票价格，整理A与B，得到x，预测第7天收盘价
N = 3
pred_prices = np.zeros(closing_prices.size - N*2)
for i in range(pred_prices.size):
	A = np.zeros((N, N))
	for j in range(N):
		A[j,:] = closing_prices[j+i:i+j+N]
	B = closing_prices[N+i:N*2+i]
	x = np.linalg.lstsq(A, B)[0]
	# dot点积：B[0]*x[0] + B[1]*x[1] + B[2]*x[2]
	pred = B.dot(x)
	pred_prices[i] = pred

mp.plot(dates[N*2:], pred_prices, 'o-', 
	color='orangered', label='Prediction Price')


mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
