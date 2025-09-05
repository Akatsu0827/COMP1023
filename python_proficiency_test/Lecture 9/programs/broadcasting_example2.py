# Filename: broadcasting_example2.py
    
import numpy as np

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]])
v = np.array([2, 1, 2])
vv = np.tile(v, (4, 1))   # Stack 4 copies of v on top of each other
print(vv)                 # Output: [[2 1 2]
                          #          [2 1 2]
                          #          [2 1 2]
                          #          [2 1 2]]
y = x + vv                # Add x and vv elementwise

print(y)                  # Output: [[ 4  4  6] 
                          #          [ 7  7  9]
                          #          [10 10 12]
                          #          [13 13 15]]