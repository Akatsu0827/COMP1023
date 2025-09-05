# Filename: series_masking.py        
import pandas as pd

s = pd.Series([10, 15, 25, 5, 30], 
              index=['a', 'b', 'c', 'd', 'e'])
mask = (s > 10) & (s < 30)  # Create a mask for values between 10 and 30
print(mask)
s[mask] = 0  # Modify elements of s where mask is True
print(s)