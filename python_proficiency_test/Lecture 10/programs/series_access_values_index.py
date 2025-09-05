# Filename: series_access_values_index.py

import pandas as pd

# Create a series with specific index
s = pd.Series([10, 20, 30, 40], index=['first', 'second', 'third', 'fourth'])
print(s.values)  # Return a NumPy array
print(s.index)   # Return an Index object