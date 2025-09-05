# Filename: transpose_example.py

import numpy as np

a = np.array([[5, 6], [7, 8]])
print(a)               # Output [[5 6]
                       #         [7 8]]
print(a.T)             # Output [[5 7]
                       #         [6 8]]
print(np.transpose(a)) # Output [[5 7]
                       #         [6 8]]
print(a.transpose())   # Output [[5 7]
                       #         [6 8]]