# Filename: dataframe_access6.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})

# Create a mask for cities with population greater than 
# 10 million and area less than 7000 sq km
mask = (df['Population'] > 10000000) & \
       (df['Area (sq km)'] < 7000)

# Print the filtered DataFrame based on the mask
print(df.loc[mask, 'Population':])