# Filename: dataframe_access2.py    
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35],
    'Salary': [70000, 80000, 120000]
}

df = pd.DataFrame(data)

arr = df.values  # Convert DataFrame to NumPy array
print(arr)  