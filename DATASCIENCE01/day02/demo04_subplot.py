"""
demo04_subplot.py  子图
"""
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Subplot', facecolor='lightgray')
for i in range(1, 10):
	mp.subplot(3,3,i)
	mp.text(0.5, 0.5, i, size=36, ha='center',
		va='center', alpha=0.6)
	mp.xticks([])
	mp.yticks([])
	mp.tight_layout()
mp.show()