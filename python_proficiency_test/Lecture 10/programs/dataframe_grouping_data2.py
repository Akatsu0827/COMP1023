# Filename: dataframe_grouping_data2.py
import pandas as pd

# Create a DataFrame with employee data
df = pd.DataFrame({'Department': ['HR', 'IT', 'HR', 'IT'],
                   'Salary': [50000, 60000, 55000, 70000],
                   'Experience': [2, 5, 3, 7]})

# 2 groups: 'HR' and 'IT'                   
groupedDf = df.groupby('Department')

# Mean salary and experience, separately for each group
result = groupedDf.mean().reset_index()
print(result)