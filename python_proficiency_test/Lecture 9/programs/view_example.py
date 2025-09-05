# Filename: view_example.py

import numpy as np
arr = np.array([1, 2, 3])
view_arr = arr[1:3]  # Creates a view
view_arr[0] = 10     # Modifies arr
print(arr)           # Print [ 1 10 3]