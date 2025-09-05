# Filename: copy_example.py

import numpy as np
import copy
original = np.array([1, 2, 3])
copy_list = copy.copy(original)  # Creates a shallow copy
copy_list[0] = 10                # Does not affect original
print(original)                  # Print [1 2 3]