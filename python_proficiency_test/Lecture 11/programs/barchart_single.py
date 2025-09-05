# Filename: barchart_single.py
import numpy as np
import matplotlib.pyplot as plt

# Position of the bars on the x-axis
x = [1, 2, 3]
# The height of each bar
height = [10, 2, 8]

labels = ["Sensor 1", "Sensor 2", "Sensor 3"]
fig, ax = plt.subplots(figsize=(3, 2))
ax.bar(x, height, tick_label=labels)
plt.show()