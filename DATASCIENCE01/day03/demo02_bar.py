"""
demo02_bar.py  柱状图
"""
import numpy as np
import matplotlib.pyplot as mp

apples = np.array(
	[46,89,19,83,61,92,86,51,29,83,74,61])
oranges = np.array(
	[98,12,33,65,12,89,65,19,85,61,82,45])
mp.figure('Bar Chart', facecolor='lightgray')
mp.title('Bar Chart', fontsize=18)
mp.grid(linestyle=':', axis='x')
mp.xlabel('Month', fontsize=14)
mp.ylabel('Volume', fontsize=14)
x = np.arange(apples.size)
mp.bar(x-0.2, apples, 0.4, color='dodgerblue',
	label='Apple', align='center')
mp.bar(x+0.2, oranges, 0.4, color='orangered',
	label='Orange', align='center')
mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 
	'May', 'Jun', 'Jul', 'Aug', 'Sep', 
	'Otc', 'Nov', 'Dec'])
mp.legend()
mp.show()






