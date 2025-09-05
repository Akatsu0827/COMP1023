# Filename: series_create.py
    
import pandas as pd

# Creating a Series without specifying an index
s1 = pd.Series([10, 20, 30, 40])
print(s1)

# Creating a Series with a custom index
s2 = pd.Series([10, 20, 30, 40], 
               index=['first', 'second', 'third', 'fourth'])
print(s2)

# Creating a Series from a dictionary
data = {'first': 10, 'second': 20, 'third': 30, 'fourth': 40}
s3 = pd.Series(data)
print(s3)