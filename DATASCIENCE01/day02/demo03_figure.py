"""
demo03_figure.py  窗口操作
"""
import matplotlib.pyplot as mp

mp.figure('Figure AAA', facecolor='lightgray')
mp.title('Figure AAA', fontsize=16)
mp.grid(linestyle=':')

mp.figure('Figure BBB', facecolor='gray')
mp.title('Figure BBB', fontsize=16)
mp.grid(linestyle='-.')

mp.figure('Figure AAA')
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tight_layout()

mp.show()
