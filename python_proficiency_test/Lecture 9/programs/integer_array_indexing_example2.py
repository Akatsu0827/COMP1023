# Filename: integer_array_indexing_example2.py

import numpy as np

# Create a new array from which we will select elements
a = np.array([[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]])

print(a)  # Output: [[13 14 15]
          #          [16 17 18]
          #          [19 20 21]
          #          [22 23 24]]

b = np.array([1, 0, 2, 1])  # Create an array of indices
# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Output: [14 16 21 23]
# Modify one element from each row of a using the indices in b
a[np.arange(4), b] += 5

print(a)  # Output: [[13 19 15]
          #          [21 17 18]
          #          [19 20 26]
          #          [22 28 24]]