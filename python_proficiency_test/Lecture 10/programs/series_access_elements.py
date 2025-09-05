# Filename: series_access_elements.py

import pandas as pd

# Create a series with specific index
s = pd.Series([10, 20, 30, 40], index=['first', 'second', 'third', 'fourth'])

# Access the element by label (element associated with index 'second')
e1 = s.loc['second']
print(e1)  # Print 20

# Access the element in position 2 (3rd element)
e2 = s.iloc[2]
print(e2)  # Print 30