# Filename: array_math_example.py

import numpy as np

x = np.array([[2, 3], [4, 5]], dtype=np.float64)
y = np.array([[6, 7], [8, 9]], dtype=np.float64)

# Elementwise sum; both yield the array
# [[ 8.0 10.0]
#  [12.0 14.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both yield the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both yield the array
# [[12.0 21.0]
#  [32.0 45.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both yield the array
# [[0.33333333 0.42857143]
#  [0.5        0.55555556]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; yields the array
# [[1.41421356 1.73205081]
#  [2.         2.23606798]]
print(np.sqrt(x))