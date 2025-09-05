# Filename: dtype_example.py

import numpy as np

x = np.array([3, 4])   # Allow NumPy to infer the data type
print(x.dtype)         # Output: int64

x = np.array([3.5, 4.5])   # Allow NumPy to infer the data type
print(x.dtype)             # Output: float64

x = np.array([3, 4], dtype=np.float32)   # Specify a specific data type
print(x.dtype)                           # Output: float32