# Filename: newaxis_example2.py

import numpy as np

array1 = np.array([[7, 8, 9], [10, 11, 12]])
print(array1)  # Output: [[ 7  8  9]
               #          [10 11 12]]

# np.newaxis adds a new dimension of size 1, i.e., 1 column
array2 = array1[:, :, np.newaxis]  # Equivalent to array2 = array1[..., np.newaxis]

print(array2)  # Output: [[[ 7] 
               #           [ 8] 
               #           [ 9]]
               #          [[10]
               #           [11]
               #           [12]]]

print(array2.shape) # Output: (2, 3, 1), indicating 2 layers, 3 rows, and 1 column