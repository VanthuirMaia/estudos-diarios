import numpy as np

arr1 = np.array([10, 21, 32, 43, 48, 15, 76, 57, 89])

indices = [1, 2, 5, 6]

print(arr1[indices])

mask = (arr1 % 2 == 0)

print(arr1[mask])

