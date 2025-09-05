# Filename: scatterplot.py
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(20)
y = np.random.rand(20)

# Color as a function of the positions of the points
colors = x + y
# Size as a function of the positions of the points
area = 100 * (x + y)
fig, ax = plt.subplots(figsize=(3, 2))

# Specify the colormap as "spring"
ax.scatter(x, y, c=colors, cmap="spring", s=area)
plt.show()