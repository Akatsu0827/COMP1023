# Filename: dataframe_create4.py
import pandas as pd

data_dict = {
    "Name": ["Emma", "Liam", "Noah"],
    "Age": [28, 32, 27],
    "City": ["Beijing", "Shanghai", "Guangzhou"]
}

df = pd.DataFrame(data_dict)
print(df)