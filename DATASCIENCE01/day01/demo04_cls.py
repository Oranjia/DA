"""
demo04_cls.py   复合数据类型 
"""
import numpy as np

data = [('zs', [81, 82, 83], 13),
		('ls', [84, 85, 86], 14),
		('ww', [87, 88, 89], 15)]
# 1. 
ary = np.array(data, dtype='U2, 3int32, int32')
print(ary, ary[2][1])

# 2. 为字段起别名
ary = np.array(data, dtype=[('name', 'str_', 2), 
							('scores', 'int32', 3), 
							('age', 'int32', (1,))])
print(ary[2]['scores'])

# 3. 为字段起别名
ary = np.array(data, dtype={
	'names' : ['name', 'scores', 'age'],
	'formats' : ['U2', '3int32', 'int32']})
print(ary, ary[2]['name'])

#第四种设置dtype的方式  
d = np.array(data, dtype={'name': ('U3', 0),
                    'scores': ('3int32', 16),
                    'age': ('int32', 28)})
print(d[0]['name'], d[0]['scores'], d.itemsize)


# 测试日期数据类型
dates = np.array(['2011', '2011-01-01', 
	'2011-02', '2011-11-11 11:11:11',
	'2012-01-01'])
print(dates, dates.dtype)
dates = dates.astype('M8[D]') # 转成日期
print(dates, dates.dtype)
print(dates[-1] - dates[0])
