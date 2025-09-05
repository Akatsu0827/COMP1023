# Filename: line_curve_draw.py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 3))
# Line through (x,y) -> (0,0), (2,4), (4,16), (6,36), (8, 64)
ax.plot([0, 2, 4, 6, 8], [0, 4, 16, 36, 64], 
        marker='o', label="Data Points 1")
# Another line through (x,y) -> (0,3), (4,7), (8,50)
ax.plot([0, 4, 8], [3, 7, 50], 
        marker='x', label="Data Points 2")

ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
ax.set_title("Sample Plot of X vs Y") 
plt.show()