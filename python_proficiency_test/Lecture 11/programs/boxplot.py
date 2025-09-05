# Filename: boxplot.py
import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, notch=True, patch_artist=True, 
            boxprops=dict(facecolor='lightblue', 
            color='blue'), medianprops=dict(color='red'))
plt.title("Box Plot of Random Data")
plt.xlabel("Dataset"); plt.ylabel("Value")
plt.xticks([1, 2, 3], ['Data 1', 'Data 2', 'Data 3'])
plt.show()