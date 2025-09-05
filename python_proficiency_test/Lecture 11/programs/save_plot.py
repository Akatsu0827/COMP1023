# Filename: save_plot.py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(3, 2))

ax.plot([0, 1, 2], [2, 4, 6])
ax.plot([0, 1, 2], [3, 6, 9])

fig.savefig("test.png") # or .jpg, .eps, .pdf