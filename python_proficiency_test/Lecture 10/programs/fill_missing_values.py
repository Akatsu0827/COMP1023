# Filename: fill_missing_values.py
import numpy as np
import pandas as pd

# Create a Series with missing values
s = pd.Series([10, 20, None, 30, np.nan])
mean_value = s.mean()
print(s.fillna(mean_value))
print()

# Create a DataFrame with missing values
df = pd.DataFrame({'Sales': [100, 200, 300], 
                   'Profit': [20, np.nan, 50]},
                  index=['Q1', 'Q2', 'Q3'])
mean_profit = df['Profit'].mean()
print(df.fillna(mean_profit)) 