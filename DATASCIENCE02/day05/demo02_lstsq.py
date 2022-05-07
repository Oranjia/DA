"""
demo02_lstsq.py  趋势线
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
	linestyle='--', alpha=0.3)

# 计算趋势点， 绘制所有趋势点
trend_points = (highest_prices + closing_prices + \
		lowest_prices) / 3
mp.scatter(dates, trend_points, s=80, 
	color='orangered', label='Trent Points')
# 整理A与B，调用lstsq方法求得线性拟合方程的k与b
days = dates.astype('M8[D]').astype('int32')
A = np.column_stack((days, np.ones_like(days)))
B = trend_points
x = np.linalg.lstsq(A, B)[0]
# 把days当做x，执行目标函数，求得每天趋势线上的价格
y = x[0] * days + x[1]
mp.plot(dates, y, color='orangered', 
	label='Trend Line')


mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
