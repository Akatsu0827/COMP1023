# Filename: series_dataframe_unary_op.py
import pandas as pd

# Creating a DataFrame with temperature data
temperature = pd.Series([32.0, 75.0, 68.5], 
                 index=['Monday', 'Tuesday', 'Wednesday'])
df = pd.DataFrame({'Temperature (F)': temperature})

# Example of unary operation: 
# converting Fahrenheit to Celsius
df['Temperature (C)'] = (df['Temperature (F)'] - 32) * 5/9
print(df)