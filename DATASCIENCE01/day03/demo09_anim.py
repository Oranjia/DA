"""
demo09_anim.py  动画
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

def update(number):
	print(number)

mp.figure("A")
a=ma.FuncAnimation(mp.gcf(), update, interval=30)
mp.show()