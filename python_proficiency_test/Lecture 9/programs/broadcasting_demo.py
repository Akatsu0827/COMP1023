# Filename: broadcasting_demo.py

import numpy as np

# We will add the vector v to every row of the matrix x,
# and store the results in the matrix y
x = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]])
v = np.array([2, 1, 2])
y = x + v  # Add v to each row of x using broadcasting
print(y)   # Print [[ 4  4  6]
           #        [ 7  7  9]
           #        [10 10 12]
           #        [13 13 15]]