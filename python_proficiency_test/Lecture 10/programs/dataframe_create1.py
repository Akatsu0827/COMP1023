# Filename: dataframe_create1.py   
import pandas as pd

sales = pd.Series([100, 150, 200], index=['Product A', 'Product B', 'Product C'])
cost = pd.Series([80, 90, 120], index=['Product A', 'Product B', 'Product C'])
units_sold = pd.Series([20, 30, 15], index=['Product A', 'Product B', 'Product C'])

df = pd.DataFrame({'Sales': sales, 'Cost': cost, 'Units Sold': units_sold})
print(df)