# Filename: histogram.py
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000) # Generate random data

plt.hist(data, bins=30, color='blue', 
         alpha=0.7, edgecolor='black')
plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()