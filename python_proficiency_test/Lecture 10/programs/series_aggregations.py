# Filename: series_aggregations.py
import pandas as pd

# Creating a Series with city populations
populations = pd.Series([21540000, 10000000, 8000000],
                 index=['Shanghai', 'Beijing', 'Chongqing'])

# Calculating the mean population
mean_population = populations.mean()
print(f'Mean Population: {mean_population}')