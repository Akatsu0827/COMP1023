# Filename: checking_missing.py
import numpy as np
import pandas as pd

# Creating a Series with null values for city populations
s = pd.Series([21540000, None, 8000000, np.nan], 
              index=['Shanghai', 'Beijing', 
                     'Chongqing', 'Guangzhou'])
# Checking for null values
null_mask = s.isnull()
print(null_mask)