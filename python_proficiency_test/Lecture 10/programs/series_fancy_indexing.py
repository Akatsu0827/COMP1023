# Filename: series_fancy_indexing.py        
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50], 
              index=['first', 'second', 'third', 'fourth', 'fifth'])
print(s.loc[['first', 'third']])  # Access indices 'first' and 'third'
print(s.iloc[[0, 2]])             # Access positions 0 and 2