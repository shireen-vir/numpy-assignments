import numpy as np

# Q1 - Numpy basics, let's go

# 1. array from 1 to 20
arr = np.arange(1, 21)
print("Array:", arr)

# 2. shape, size, dtype
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Dtype:", arr.dtype)

# 3. convert to float
arr_float = arr.astype(float)
print("Float array:", arr_float)

# 4. sum and mean
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
