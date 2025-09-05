# Filename: dataframe_drop_column.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'],
                 index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000],
                        index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], 
                  index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 
                   'Area (sq km)': area})
print(df)  # Display the original DataFrame
# Drop the 'Population' and 'Area (sq km)' columns
df = df.drop(columns=['Population', 'Area (sq km)'])
print(df)  # Display the DataFrame after dropping columns