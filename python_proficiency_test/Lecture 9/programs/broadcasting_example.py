# Filename: broadcasting_example.py
        
import numpy as np

# We will add the vector v to each row of the matrix x, storing the result in y
x = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]])
v = np.array([2, 1, 2])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x using an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v

print(y)  # Output: [[ 4  4  6] 
          #          [ 7  7  9]
          #          [10 10 12]
          #          [13 13 15]]