# Filename: remove_missing.py
import numpy as np
import pandas as pd

# Creating a Series with missing values for city populations
s = pd.Series([21540000, None, 8000000, np.nan], 
              index=['Shanghai', 'Beijing', 
                     'Chongqing', 'Guangzhou'])
print("Original Series:")
print(s)
print("\nSeries after dropping missing values:")
print(s.dropna())
print()

# Creating a DataFrame with missing values for city statistics
df = pd.DataFrame({'Population': [21540000, 10000000, None], 
                   'Area (sq mi)': [2400.0, np.nan, 315.0]},
                  index=['Shanghai', 'Beijing', 'Chongqing'])
print("Original DataFrame:")
print(df)                  
print("\nDataFrame after dropping missing values:")
print(df.dropna())   