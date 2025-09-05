# Filename: dataframe_access5.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})

# Access columns from 'Population' to 'Area (sq km)' and rows from 'B' to 'C'                   
print(df.loc['B':'C', 'Population':'Area (sq km)'])