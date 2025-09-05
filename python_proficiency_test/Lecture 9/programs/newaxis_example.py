# Filename: newaxis_example.py

import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
print(array1)  # Output: [10 20 30 40 50]

# Convert 1D array to a row vector
array2 = array1[np.newaxis]
print(array2)  # Output: [[10 20 30 40 50]]

# Convert 1D array to a row vector using None
array3 = array1[None]
print(array3)  # Output: [[10 20 30 40 50]]

array4 = np.array([[7, 8, 9], [10, 11, 12]])
print(array4)  # Output: [[ 7  8  9]
               #          [10 11 12]]

array5 = array4[np.newaxis]
print(array5)  # Output: [[[ 7  8  9]
               #           [10 11 12]]]