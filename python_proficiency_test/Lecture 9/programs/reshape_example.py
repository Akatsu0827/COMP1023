# Filename: reshape_example.py

import numpy as np

array1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
array2 = array1.reshape(4, 3)   # Reshape array1 into a 2D array with 4 rows and 3 columns
# array2 = array1.reshape(4, -1) # This line achieves the same result as array1.reshape(4, 3)
print(array2) # Output [[ 10  20  30]
               #         [ 40  50  60]
               #         [ 70  80  90]
               #         [100 110 120]]
print("Shape of array2:", array2.shape) # Output Shape of array2: (4, 3)