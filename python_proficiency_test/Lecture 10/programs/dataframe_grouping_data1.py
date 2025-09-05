# Filename: dataframe_grouping_data1.py
import pandas as pd

# Create a DataFrame with sales data
df = pd.DataFrame({'Region': ['North', 'South', 'North', 'South'],
                   'Sales': [250, 150, 300, 200],
                   'Profit': [50, 30, 70, 40]})
groupedDf = df.groupby('Region') # 2 groups: 'North' and 'South'                   

for key, groupDf in groupedDf:
    print(key)
    print(groupDf)