# Filename: series_slicing.py        
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50, 60], 
       index=['first', 'second', 'third', 'fourth', 'fifth', 'sixth'])
# Slicing with explicit index (both included)              
print(s.loc['third':'fifth'])
# Slicing with implicit index 
# (start included and stop excluded)
print(s.iloc[2:5])