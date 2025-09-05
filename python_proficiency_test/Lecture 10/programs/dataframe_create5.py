# Filename: dataframe_create5.py        
import numpy as np
import pandas as pd

# Create a 2D NumPy array with data related to cities in China
arr = np.array([[28, 32, 27],  # Ages
                 [1, 2, 3],    # IDs or similar identifiers
                 [1, 0, 1]])   # Some binary data (e.g., availability of a service)
                 
# Create a DataFrame from the array
df = pd.DataFrame(arr, columns=['Beijing', 'Shanghai', 'Guangzhou'], 
                  index=['Age', 'ID', 'Service Available'])
print(df)