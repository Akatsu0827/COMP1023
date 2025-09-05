# Filename: dataframe_add_column.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})

# Adding a new column to indicate if the city is coastal
df['Is Coastal'] = pd.Series([False, True, False], index=['A', 'B', 'C'])
# The above is equivalent to df['Is Coastal'] = [False, True, False]                            
print(df) 