"""
demo05_polyfit.py  多项式拟合
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

# 计算差价函数
diff_prices = bhp_closing_prices - vale_closing_prices

mp.plot(dates, diff_prices, color='dodgerblue',
	label='diff Price', linewidth=1,
	linestyle='--')

# 拟合这组数据，得到多项式函数方程
x = dates.astype('M8[D]').astype('int32')
y = diff_prices
P = np.polyfit(x, y, 4)
pred_y = np.polyval(P, x)
mp.plot(dates, pred_y, color='orangered', 
	linewidth=2)

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()




