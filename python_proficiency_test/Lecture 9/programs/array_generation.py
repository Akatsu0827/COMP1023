# Filename: array_generation.py

import numpy as np

a = np.zeros((3,3))          # Generate an array filled with zeros
print(a)                     # Output: [[ 0.  0.  0.]
                             #          [ 0.  0.  0.]
                             #          [ 0.  0.  0.]]
b = np.ones((2,3))           # Generate an array filled with ones
print(b)                     # Output: [[ 1.  1.  1.]
                             #          [ 1.  1.  1.]]

c = np.full((3,2), 5)        # Generate an array with a constant value
print(c)                     # Output: [[ 5  5]
                             #          [ 5  5]
                             #          [ 5  5]]
d = np.eye(3)                # Generate a 3x3 identity matrix
print(d)                     # Output: [[ 1.  0.  0.]
                             #          [ 0.  1.  0.]
                             #          [ 0.  0.  1.]]
e = np.random.rand(3,2)      # Generate an array with random values
print(e)                     # Output: [[ 0.12345678  0.87654321]
                             #          [ 0.23456789  0.76543210]
                             #          [ 0.34567890  0.65432109]]