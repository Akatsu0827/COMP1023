# Filename: effect_of_operations.py

import numpy as np # Import NumPy package

ls = [1, 2, 3]      # Declare a list
arr = np.array(ls)  # Convert the list into a NumPy array

try:
    ls = ls + 4    # Add 4 to each element of the list
except TypeError:
    print("Lists don't support list + int")

# Now on the array
try:
    arr = arr + 4  # Add 4 to each element of the NumPy array
    print("Modified NumPy array: ", arr)  # Print the NumPy array
except TypeError:
    print("NumPy arrays don't support array + int")