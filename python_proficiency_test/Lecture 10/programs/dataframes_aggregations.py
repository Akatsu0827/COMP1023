# Filename: dataframes_aggregations.py
import pandas as pd

# Creating a DataFrame with city population and area data
data = {
    'City': ['Shanghai', 'Beijing', 'Chongqing'],
    'Population': [21540000, 10000000, 8000000],
    'Area (sq mi)': [2400.0, 1687.0, 315.0]
}
df = pd.DataFrame(data)

# Calculating aggregate functions for the DataFrame
mean_values = df[['Population', 'Area (sq mi)']].mean()
print(mean_values)