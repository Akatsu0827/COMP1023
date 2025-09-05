# Filename: series_assign_values.py        
import pandas as pd

# Create a series with specific index
s = pd.Series([10, 20, 30], index=['first', 'second', 'third'])
print(s.loc['first'])  # Access with explicit index
print(s.iloc[0])       # Access with implicit index
s.loc['second'] = 50   # Assign a new value
print(s)