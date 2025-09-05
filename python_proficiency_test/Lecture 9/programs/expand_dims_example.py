# Filename: expand_dims_example.py
 
import numpy as np

array1 = np.array([[7, 8, 9], [10, 11, 12]])
print(array1)  # Output: [[ 7  8  9]
               #          [10 11 12]]

# 1 means adding a new dimension of size 1, after the 1st dimension
array2 = np.expand_dims(array1, axis=1)

print(array2)  # Output: [[[ 7  8  9]]
               #          [[10 11 12]]]

print(array2.shape) # Output: (2, 1, 3), indicating 2 layers, 1 row, and 3 columns