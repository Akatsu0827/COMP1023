# Filename: sequence_points_segments_draw.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 20)
y = np.exp(x)

fig, ax = plt.subplots(figsize=(3, 2))

ax.plot(x, y, c="blue", linestyle="", 
        marker='*', label="Curve 1")
ax.plot(x, 2*y, c="green", 
        linestyle="--", label="Curve 2")

# Specify the legend position with relative position
ax.legend(loc=(1.1, 0.5))
plt.show()