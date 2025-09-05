# Filename: csv_saving_data.py
import pandas as pd
import os

# Sample DataFrame with employee data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [60000, 75000, 80000, 90000, None],
    'Experience': [None, 5, 7, None, 3]
}
df = pd.DataFrame(data)

# Define the path to save the CSV file
path = os.path.join('./data', 'employees2.csv')
df.to_csv(path, sep=',', index=False)