# Filename: series_op.py
import pandas as pd

# Creating two Series with city populations
city_a = pd.Series([21540000, 10000000, 8000000], 
            index=['Shanghai', 'Beijing', 'Chongqing'])
city_b = pd.Series([1000000, 2000000, 3000000], 
            index=['Beijing', 'Chongqing', 'Guangzhou'])
result = city_a + city_b
print(result)