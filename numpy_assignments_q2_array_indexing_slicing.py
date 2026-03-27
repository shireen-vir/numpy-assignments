import numpy as np

# Q2 - indexing and slicing stuff

# 1. 15 random integers between 10 and 50
arr = np.random.randint(10, 51, size=15)
print("Original array:", arr)

# 2. first and last 5 elements
print("First 5:", arr[:5])
print("Last 5:", arr[-5:])

# 3. replace values > 30 with 0
arr_copy = arr.copy()
arr_copy[arr_copy > 30] = 0
print("After replacing >30 with 0:", arr_copy)

# 4. elements at even indices (0, 2, 4...)
print("Even index elements:", arr[::2])
