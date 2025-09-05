# Filename: mean_func.py
 
import numpy as np

y = np.array([[5, 10], [15, 20]])

print(np.mean(y))          # Calculate the mean of all elements; output 12.5
print(np.mean(y, axis=0))  # Calculate the mean of each column; output [10. 15.]
print(np.mean(y, axis=1))  # Calculate the mean of each row; output [7.5 17.5]