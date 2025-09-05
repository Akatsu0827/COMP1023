# Filename: dataframe_create3.py
import pandas as pd

data1 = [{'name': 'Emma', 'age': 28, 'city': 'Beijing'},
         {'name': 'Liam', 'age': 32, 'city': 'Shanghai'},
         {'name': 'Noah', 'age': 27, 'city': 'Guangzhou'}]
df1 = pd.DataFrame(data1)
print(df1)

data2 = [{'name': 'Sophie', 'age': 29, 'city': 'Shenzhen'},
         {'name': 'Oliver', 'age': 31, 'city': 'Chengdu'},
         {'name': 'Ava', 'age': 26, 'city': 'Hangzhou'}]
df2 = pd.DataFrame(data2, index=['row1', 'row2', 'row3'])
print(df2)