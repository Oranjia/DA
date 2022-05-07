"""
demo05_grid.py   网格布局
"""
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure('Grid', facecolor='lightgray')
gs = mg.GridSpec(3, 3)

mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, '1', size=36, ha='center',
		va='center', alpha=0.6)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[:2, 2])
mp.text(0.5, 0.5, '2', size=36, ha='center',
		va='center', alpha=0.6)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[1, 1])
mp.text(0.5, 0.5, '3', size=36, ha='center',
		va='center', alpha=0.6)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[1:, 0])
mp.text(0.5, 0.5, '4', size=36, ha='center',
		va='center', alpha=0.6)
mp.xticks([])
mp.yticks([])
mp.tight_layout()

mp.subplot(gs[-1, 1:])
mp.text(0.5, 0.5, '5', size=36, ha='center',
		va='center', alpha=0.6)
mp.xticks([])
mp.yticks([])
mp.tight_layout()


mp.show()