# Filename: time_comparison.py

import numpy as np       # Import required packages
import time as t

size = 1000000           # Size of arrays and lists

list1 = range(size)      # Declare lists
list2 = range(size)
array1 = np.arange(size) # Declare arrays
array2 = np.arange(size)

# Capture time before the multiplication of Python lists
initialTime = t.time()
# Multiply elements of both lists and store in another list
resultList = [(a * b) for a, b in zip(list1, list2)]
# Calculate execution time, it prints "Time taken by Lists: 0.13024258613586426 s"
print("Time taken by Lists:", (t.time() - initialTime), "s")

# Capture time before the multiplication of NumPy arrays
initialTime = t.time()
# Multiply elements of both NumPy arrays and store in another NumPy array
resultArray = array1 * array2
# Calculate execution time, it prints "Time taken by NumPy Arrays: 0.006006956100463867 s"
print("Time taken by NumPy Arrays:", (t.time() - initialTime), "s")