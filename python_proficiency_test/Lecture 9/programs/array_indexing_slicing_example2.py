# Filename: array_indexing_slicing_example2.py

import numpy as np

# Create a rank 2 array with shape (3, 4)
# [[ 11  12  13  14]
#  [ 15  16  17  18]
#  [ 19  20  21  22]]
a = np.array([[11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]])

# Mixing integer indexing with slices yields an array of lower rank, 
# while using only slices yields an array of the same rank as the original:
row_r1 = a[2, :]    # Rank 1 view of the third row of a
row_r2 = a[2:3, :]  # Rank 2 view of the third row of a
print(row_r1, row_r1.shape)  # Output: [19 20 21 22] (4,)
print(row_r2, row_r2.shape)  # Output: [[19 20 21 22]] (1, 4)

# The same distinction applies when accessing columns of an array:
col_r1 = a[:, 2]
col_r2 = a[:, 2:3]
print(col_r1, col_r1.shape)  # Output: [13 17 21] (3,)
print(col_r2, col_r2.shape)  # Output: [[13]
                             #          [17]
                             #          [21]] (3, 1)