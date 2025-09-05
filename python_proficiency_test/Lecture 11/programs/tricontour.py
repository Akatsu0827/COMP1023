# Filename: tricontour.py    
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

x = np.random.rand(30); y = np.random.rand(30)
z = np.sin(x) + np.cos(y)
triang = Triangulation(x, y) # Create triangulation

plt.tricontour(triang, z, levels=14, cmap='plasma')
plt.colorbar(label='Z Value')
plt.title("Triangular Contour Plot")
plt.xlabel("X-axis"); plt.ylabel("Y-axis")
plt.show()