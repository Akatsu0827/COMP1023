# Filename: dataframe_access3.py    
import pandas as pd

temperature = pd.Series([22.5, 23.0, 19.5], index=['Monday', 'Tuesday', 'Wednesday'])
humidity = pd.Series([55, 60, 50], index=['Monday', 'Tuesday', 'Wednesday'])
wind_speed = pd.Series([5.5, 3.0, 7.2], index=['Monday', 'Tuesday', 'Wednesday'])
df = pd.DataFrame({'Temperature': temperature, 'Humidity': humidity, 
                   'Wind Speed': wind_speed})

print(df["Humidity"]) 