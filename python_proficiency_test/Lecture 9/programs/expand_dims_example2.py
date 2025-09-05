# Filename: expand_dims_example2.py
   
import numpy as np

array1 = np.array([[13, 14, 15], [16, 17, 18]])
print(array1)  # Output: [[13 14 15]
               #          [16 17 18]]

# 2 means adding a new dimension of size 1, after the 2nd dimension
array2 = np.expand_dims(array1, axis=2)

print(array2)  # Output: [[[13]
               #           [14]
               #           [15]]
               #          [[16]
               #           [17]
               #           [18]]]

print(array2.shape) # Output: (2, 3, 1), indicating 2 layers, 3 rows, and 1 column