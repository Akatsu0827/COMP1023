# Filename: array_indexing_slicing_example.py

import numpy as np

# Create a rank 2 array with shape (3, 4)
# [[10  20  30  40]
#  [50  60  70  80]
#  [90 100 110 120]]
a = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
# Use slicing to extract a subarray containing the first 2 rows
# and columns 2 and 3; b will be the following array of shape (2, 2):
# [[30 40]
#  [70 80]]
b = a[:2, 2:4]
# A slice of an array is a view of the original data, so changing it
# will also change the original array.
print(a[0, 2])   # Output: 30
b[0, 0] = 99     # b[0, 0] refers to the same data as a[0, 2]
print(a[0, 2])   # Output: 99