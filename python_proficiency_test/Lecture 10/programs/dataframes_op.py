# Filename: dataframes_op.py
import pandas as pd

# Creating two DataFrames with city populations and areas
df1 = pd.DataFrame([[21540000, 2400.0], [10000000, 1687.0], 
                    [8000000, 315.0]],
                   columns=['Population', 'Area (sq mi)'],
                   index=['Shanghai', 'Beijing', 'Chongqing'])
print(df1)        
          
df2 = pd.DataFrame([[1000000, 743.0], [2000000, 400.0]],
                   columns=['Population', 'Area (sq mi)'],
                   index=['Beijing', 'Guangzhou'])
print(df2)

print(df1 + df2) # Adding the two DataFrames