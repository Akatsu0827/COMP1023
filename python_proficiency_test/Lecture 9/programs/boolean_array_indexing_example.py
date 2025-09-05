# Filename: boolean_array_indexing_example.py

import numpy as np

a = np.array([[7, 8], [9, 10], [11, 12]])

bool_idx = (a < 10)   # Identify elements of a that are less than 10; this creates a numpy 
                      # array of Booleans with the same shape as a, where each entry in bool_idx 
                      # indicates whether the corresponding element of a is < 10.

print(bool_idx)      # Output: [[ True  True]
                      #         [ True False]
                      #         [False False]]

# Use boolean array indexing to create a rank 1 array of the elements of a 
# corresponding to the True values in bool_idx
print(a[bool_idx])  # Output: [7 8 9]

# All of the above can be done in one concise statement:
print(a[a < 10])    # Output: [7 8 9]