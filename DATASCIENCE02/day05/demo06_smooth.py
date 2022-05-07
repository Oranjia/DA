"""
demo06_smooth.py  数据平滑
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md
import datetime as dt

def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	t = time.strftime('%Y-%m-%d')
	return t

dates, bhp_closing_prices = np.loadtxt(
	'../da_data/bhp.csv', delimiter=',', 
	usecols=(1,6), dtype='M8[D], f8',
	converters={1:dmy2ymd}, unpack=True)

vale_closing_prices = np.loadtxt( 
	'../da_data/vale.csv', delimiter=',', 
	usecols=(6,))

bhp_returns = np.diff(bhp_closing_prices) / bhp_closing_prices[:-1]
vale_returns = np.diff(vale_closing_prices) / vale_closing_prices[:-1]

#绘制这条曲线
mp.figure('BHP VALE RETURNS', facecolor='lightgray')
mp.title('BHP VALE RETURNS', fontsize=20)
mp.xlabel('Date')
mp.ylabel('Price')
mp.grid(linestyle=':')
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%Y %m %d'))
dates = dates.astype('M8[D]').astype(md.datetime.datetime)
dates = dates[:-1]
#绘制收益线
mp.plot(dates, bhp_returns, color='dodgerblue', 
	linestyle='--', label='bhp_returns', alpha=0.2)
mp.plot(dates, vale_returns, color='orangered', 
	linestyle='--', label='vale_returns', alpha=0.2)


#卷积降噪
convolve_core = np.hanning(8)
convolve_core /= convolve_core.sum()
bhp_returns_convolved = np.convolve(
	bhp_returns, convolve_core, 'valid')
vale_returns_convolved = np.convolve(
	vale_returns, convolve_core, 'valid')

#绘制卷积降噪线
mp.plot(dates[7:], bhp_returns_convolved, 
	color='dodgerblue', label='bhp_returns_convolved', 
	alpha=0.4)
mp.plot(dates[7:], vale_returns_convolved, 
	color='orangered', label='vale_returns_convolved', 
	alpha=0.4)

# 针对卷积结果，做多项式拟合
days = dates[7:].astype('M8[D]').astype('int32')
p_bhp = np.polyfit(days, bhp_returns_convolved, 3)
p_vale = np.polyfit(days, vale_returns_convolved, 3)
polyline_bhp = np.polyval(p_bhp, days)
polyline_vale = np.polyval(p_vale, days)
mp.plot(dates[7:], polyline_bhp, 
	color='dodgerblue', label='polyline_bhp', 
	alpha=0.9, linewidth=2)
mp.plot(dates[7:], polyline_vale, 
	color='orangered', label='polyline_vale', 
	alpha=0.9, linewidth=2)

# 通过差函数，求两条曲线的交点。
p_diff = np.polysub(p_bhp, p_vale)
xs = np.roots(p_diff)
print(xs.astype('M8[D]'))

mp.show()
