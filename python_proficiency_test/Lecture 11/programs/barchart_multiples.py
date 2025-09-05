# Filename: barchart_multiples.py
import numpy as np
import matplotlib.pyplot as plt
heightMin = [10, 2, 8]
heightMax = [8, 6, 5]
x = np.arange(3)
width = 0.4
labels = ["Sensor 1", "Sensor 2", "Sensor 3"]

fig, ax = plt.subplots(figsize=(3, 2))
# Blue bars
ax.bar(x + width / 2, heightMin, width=width, label="Min")
# Orange bars
ax.bar(x - width / 2, heightMax, width=width, label="Max")

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc=(1.1, 0.5))
plt.show()