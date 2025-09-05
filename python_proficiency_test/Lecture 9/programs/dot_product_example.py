# Filename: dot_product_example.py

import numpy as np

x = np.array([[2, 4], [6, 8]])
y = np.array([[1, 3], [5, 7]])
v = np.array([8, 9])
w = np.array([10, 11])

# Dot product of vectors; both yield 170
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both yield the rank 1 array [52 120]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both yield the rank 2 array
# [[22 34]
#  [46 74]]
print(x.dot(y))
print(np.dot(x, y))