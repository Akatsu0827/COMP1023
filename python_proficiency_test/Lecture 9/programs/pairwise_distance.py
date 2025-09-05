# Filename: pairwise_distance.py

import numpy as np

# A shape-(3, 3) array
x = np.array([[ 8.54,  1.54,  8.12],
              [ 3.13,  8.76,  5.29],
              [ 7.73,  6.71,  1.31]])

# A shape-(2, 3) array
y = np.array([[ 8.65,  0.27,  4.67],
              [ 7.73,  7.26,  1.95]])

reshaped_x = x.reshape(3, 1, 3)
reshaped_y = y.reshape(1, 2, 3)
diffs = reshaped_x - reshaped_y
print("Shape of diffs", diffs.shape)   # Print (3, 2, 3)

print(diffs)  # Print [[[-0.11  1.27  3.45]
              #         [ 0.81 -5.72  6.17]]
              #        [[-5.52  8.49  0.62]
              #         [-4.6   1.5   3.34]]
              #        [[-0.92  6.44 -3.36]
              #         [ 0.   -0.55 -0.64]]]

dists = np.sqrt(np.sum(diffs**2, axis=2))  # axis=2 refers to the column axis

print(dists)  # Print [[ 3.67797499  8.45241977]
              #        [10.14568381  5.87925165]
              #        [ 7.32185769  0.84386018]]

print(dists.shape)  # Print (3, 2), indicating 3 rows and 2 columns