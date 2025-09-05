# Filename: area_filling.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x); y2 = np.sin(x) + 0.5

plt.fill_between(x, y1, y2, color='skyblue', 
                 alpha=0.5, label='Area between curves')
plt.plot(x, y1, label='y1 = sin(x)', color='blue')
plt.plot(x, y2, label='y2 = sin(x) + 0.5', color='orange')
plt.title("Area Filling with fill_between()")
plt.xlabel("X-axis"); plt.ylabel("Y-axis")
plt.legend()
plt.show()