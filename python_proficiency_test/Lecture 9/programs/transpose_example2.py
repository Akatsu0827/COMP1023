# Filename: transpose_example2.py

import numpy as np
# Create a 3D array
# (2 layers, 4 rows, and 3 columns)
# with numbers 0 to 23.
array = np.array([[[ 0,  1,  2],
                   [ 3,  4,  5],
                   [ 6,  7,  8],
                   [ 9, 10, 11]],
                  [[12, 13, 14],
                   [15, 16, 17],
                   [18, 19, 20],
                   [21, 22, 23]]])

# The transpose function can rearrange the axes of the array.
# For instance, if we want to 
# move the current last axis (i.e., 2) 
# to the front (as axis 0),
# shift the current first axis (i.e., 0) 
# to the middle (as axis 1),
# and place the current second axis (i.e., 1) 
# at the end (as axis 2).
# We specify the order in transpose as [2, 0, 1].
print(np.transpose(array, [2, 0, 1])) 
# Equivalent output using the line below
print(array.transpose([2, 0, 1]))

# Output will be [[[ 0  3  6  9]                
#                  [12 15 18 21]]
#
#                 [[ 1  4  7 10]
#                  [13 16 19 22]]
#
#                 [[ 2  5  8 11]
#                  [14 17 20 23]]]