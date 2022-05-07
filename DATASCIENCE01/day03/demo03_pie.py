"""
demo03_pie.py   饼状图
"""
import matplotlib.pyplot as mp

#整理数据
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']
# 等轴比例
mp.figure('Pie', facecolor='lightgray')
mp.axis('equal')
mp.title('Pie', fontsize=18)
mp.pie(values, spaces, labels, colors,
	'%.1f%%', startangle=0, shadow=True)
mp.legend()
mp.show()
