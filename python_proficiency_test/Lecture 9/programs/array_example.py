# Filename: array_example.py

import numpy as np

a = np.array([10, 20, 30])            # Create a rank 1 array
print(type(a))                        # Output: <class 'numpy.ndarray'>
print(a.shape)                        # Output: (3,)
print(a[0], a[1], a[2])               # Output: 10 20 30
a[0] = 50                             # Modify an element of the array
print(a)                              # Output: [50 20 30]
b = np.array([[7, 8, 9], [10, 11, 12]]) # Create a rank 2 array
print(b.shape)                        # Output: (2, 3)
print(b[0, 0], b[0, 1], b[1, 0])      # Same as b[0][0], b[0][1], b[1][0]. Output: 7 8 10