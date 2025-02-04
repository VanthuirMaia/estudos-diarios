import numpy as np
import os
import matplotlib.pyplot as plt

"""
filename = os.path.join("DSA/Python/dataset.csv")

var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(0, 1), skiprows=1, unpack=True)

plt.plot(var1, var2, 'o', markersize=6, color = 'red')

plt.show

######################################################

arr14 = np.array([15, 23, 63, 94, 75])

print(np.mean(arr14))
print(np.std(arr14))
print(np.var(arr14))

######################################################

arr15 = np.arange(1, 10)

print(arr15)

# Soma
print(np.sum(arr15))

# Produto
print(np.prod(arr15))

# Soma Acumulada
print(np.cumsum(arr15))

arr16 = np.array([3, 2, 1])
arr17 = np.array([1, 2, 3])

arr18 = np.add(arr16, arr17)

print(arr18)

######################################################


"""

arr19 = np.array([[1, 2], [3, 4]])
arr20 = np.array([[5, 6], [0, 7]])

arr19.shape
arr20.shape

print(arr19)
print(arr20)

arr21 = np.dot(arr19, arr20)
print(arr21)