# Filename: csv_loading_data.py
import pandas as pd

# Load data from a CSV file with specific NA values
df = pd.read_csv('./data/employees.csv', 
                 sep=',', 
                 skiprows=0,
                 na_values=['N/A', 'Missing'])
print(df)