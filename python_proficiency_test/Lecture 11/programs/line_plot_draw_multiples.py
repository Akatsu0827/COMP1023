import matplotlib.pyplot as plt  # Filename: line_plot_draw_multiples.py

fig, ax = plt.subplots(2, 2, figsize=(10, 6))

ax[0, 0].plot([0, 1, 2], [2, 4, 6])  # First subplot
ax[0, 0].set_xlabel("X Values")
ax[0, 0].set_ylabel("Y Values")
ax[0, 0].set_title("Plot 1: Line through (0,2), (1,4), (2,6)")

ax[0, 1].plot([0, 1, 2], [3, 6, 9])  # Second subplot
ax[0, 1].set_xlabel("X Values")
ax[0, 1].set_ylabel("Y Values")
ax[0, 1].set_title("Plot 2: Line through (0,3), (1,6), (2,9)")

ax[1, 0].plot([0, 1, 2], [1, 2, 3])  # Third subplot
ax[1, 0].set_xlabel("X Values")
ax[1, 0].set_ylabel("Y Values")
ax[1, 0].set_title("Plot 3: Line through (0,1), (1,2), (2,3)")

ax[1, 1].plot([0, 1, 2], [4, 8, 12]) # Fourth subplot
ax[1, 1].set_xlabel("X Values")
ax[1, 1].set_ylabel("Y Values")
ax[1, 1].set_title("Plot 4: Line through (0,4), (1,8), (2,12)")

plt.tight_layout()
plt.show()