# Filename: matrix_operations.py

import numpy as np

a = np.array([[2, 3], [5, 7]])
b = np.array([[4, 1], [6, 3]])
u = np.array([8, 9])
v = np.array([10, 11])

# Inner product of vectors; both yield 170
print(np.matmul(u, v))
print(u @ v)

# Matrix / vector product; both yield the rank 1 array [43 103]
print(np.matmul(a, u))
print(a @ u)

# Matrix / matrix product; both yield the rank 2 array
# [[26 11]
#  [62 26]]
print(np.matmul(a, b))
print(a @ b)