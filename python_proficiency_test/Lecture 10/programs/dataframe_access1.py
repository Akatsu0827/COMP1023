# Filename: dataframe_access1.py
import pandas as pd

data = {
    'Name': ['Emma', 'Liam', 'Noah'],
    'Age': [28, 32, 27],
    'City': ['Beijing', 'Shanghai', 'Guangzhou']
}

df = pd.DataFrame(data)
print(df.columns)  # Index object with column names
print(df.index)    # Index object with row indices