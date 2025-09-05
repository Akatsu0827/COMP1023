# Filename: integer_array_indexing_example.py

import numpy as np

a = np.array([[7, 8], [9, 10], [11, 12]])

# An example of integer array indexing.
# The returned array will have shape (3,)
print(a[[0, 1, 2], [1, 0, 1]])  # Output: [ 8  9 12]

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 1], a[1, 0], a[2, 1]]))  # Output: [ 8  9 12]

# When using integer array indexing, you can reuse the same
# element from the source array:
print(a[[1, 1], [0, 0]])  # Output: [9 9]

# Equivalent to the previous integer array indexing example
print(np.array([a[1, 0], a[1, 0]]))  # Output: [9 9]