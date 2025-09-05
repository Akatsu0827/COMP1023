# Filename: dataframe_access7.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'],
                 index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000],
                        index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], 
                  index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 
                   'Area (sq km)': area})

# Print selected rows and columns
print(df.loc[['A', 'C'], ['City', 'Population']])

# Update selected rows and columns
df.loc[['A', 'C'], ['City', 'Population']] = ['Updated City', 0]
print(df.loc[['A', 'C'], ['City', 'Population']])