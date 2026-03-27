import numpy as np

# Q7 - reshaping and stacking arrays

# 1. 1D array of size 12
arr = np.arange(1, 13)
print("Original:", arr)

# 2. reshape to 3x4 and 2x6
mat1 = arr.reshape(3, 4)
mat2 = arr.reshape(2, 6)
print("3x4:\n", mat1)
print("2x6:\n", mat2)

# 3. vertical and horizontal stacking
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vstacked = np.vstack((a, b))
hstacked = np.hstack((a, b))
print("Vertical stack:\n", vstacked)
print("Horizontal stack:", hstacked)

# 4. flatten
flat = vstacked.flatten()
print("Flattened:", flat)
