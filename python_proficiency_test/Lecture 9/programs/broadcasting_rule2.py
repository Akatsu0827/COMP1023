# Filename: broadcasting_rule2.py
         
import numpy as np

A = np.array([1, 2, 3])
print(A.ndim)  # Print 1
print(A.shape) # Print (3,)
B = np.array([[4, 4, 4], [3, 3, 3]])
print(B.ndim)  # Print 2
print(B.shape) # Print (2, 3)
print(A * B)   # Print [[ 4  8 12]
               #        [ 3  6  9]]