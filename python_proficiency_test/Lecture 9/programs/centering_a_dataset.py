# Filename: centering_a_dataset.py

import numpy as np
scores = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])
score_mean = scores.mean(0)  # 0 indicates the first dimension
print(score_mean)            # Print array([7., 8., 9.])

scores_centered = scores - score_mean
print(scores_centered)    # Print array([[-6., -6., -6.],
                          #              [-3., -3., -3.],
                          #              [ 0.,  0.,  0.],
                          #              [ 3.,  3.,  3.],
                          #              [ 6.,  6.,  6.]])
print(scores_centered.mean(axis=0))    # Print array([0., 0., 0.])