# Filename: newaxis_example3.py

import numpy as np

array1 = np.array([[5, 6, 7], [8, 9, 10]])
print(array1)  # Output: [[ 5  6  7]
               #          [ 8  9 10]]

# np.newaxis adds a new dimension of size 1, i.e., 1 row
# highest dimension, i.e., row
array2 = array1[np.newaxis, :, :]

print(array2)  # Output: [[[ 5  6  7]
               #           [ 8  9 10]]]

print(array2.shape) # Output: (1, 2, 3), indicating 1 layer, 2 rows, and 3 columns