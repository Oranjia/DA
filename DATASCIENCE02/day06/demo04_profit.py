"""
demo04_profit.py 自定义策略 使用历史数据进行策略回测
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


def profit(open, high, low, close):
	# 定义函数   描述一种投资策略
	buy_price = open * 1.00
	if low <= buy_price <= high:
		return (close - buy_price) / buy_price
	else:
		return np.nan

# 求30天的收益率，矢量化profit函数
profits = np.vectorize(profit)(
	opening_prices, highest_prices, 
	lowest_prices, closing_prices)
print(profits)
# 判断无效值
isnan = np.isnan(profits)

# 绘制收盘价折线图
mp.figure('Profits', facecolor='lightgray')
mp.title('Profits', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Profit Return', fontsize=14)
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
# 绘制收益率折线
dates = dates[~isnan]
profits = profits[~isnan]
mp.plot(dates, profits, 'o-', color='dodgerblue',
	label='Profits')
print(profits.mean())
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
