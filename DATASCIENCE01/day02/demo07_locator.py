"""
demo07_locator.py 刻度定位器
"""
import numpy as np
import matplotlib.pyplot as mp

locators = ['mp.NullLocator()', 
			'mp.MultipleLocator(1)', 
			'mp.MaxNLocator(nbins=3)', 
			'mp.AutoLocator()']

mp.figure('Locator', facecolor='lightgray')
mp.title('Locator', fontsize=18)

for i, locator in enumerate(locators):
	mp.subplot(len(locators), 1, i+1)
	ax = mp.gca()
	ax.xaxis.set_major_locator(eval(locator))
	ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
	# ax.xaxis.set_minor_locator(mp.NullLocator())
	mp.xlim(1, 10)
	ax.spines['top'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['bottom'].set_position(('data', 0.5))
	mp.yticks([])

mp.show()


