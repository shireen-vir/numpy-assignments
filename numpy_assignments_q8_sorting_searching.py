import numpy as np

# Q8 - sorting and searching

# 1. 10 random integers
arr = np.random.randint(1, 100, size=10)
print("Original:", arr)

# 2. sort ascending and descending
asc = np.sort(arr)
desc = np.sort(arr)[::-1]
print("Ascending:", asc)
print("Descending:", desc)

# 3. max and min
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# 4. index of max value
max_idx = np.argmax(arr)
print("Index of max value:", max_idx)
