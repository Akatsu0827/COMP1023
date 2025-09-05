# Filename: broadcasting_rule1.py
  
import numpy as np

A = np.array([1, 2, 3])
print(A.ndim)     # Print 1
print(A.shape)    # Print (3,)
B = np.array([2])
print(B.ndim)     # Print 1
print(B.shape)    # Print (1,)
print(A * B)      # Print [2, 4, 6]