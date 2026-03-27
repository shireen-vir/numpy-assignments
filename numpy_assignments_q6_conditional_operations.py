import numpy as np

# Q6 - conditions and filtering

# 1. 20 random integers between 1 and 100
arr = np.random.randint(1, 101, size=20)
print("Array:", arr)

# 2. extract even numbers
evens = arr[arr % 2 == 0]
print("Even numbers:", evens)

# 3. replace odd numbers with -1
arr_copy = arr.copy()
arr_copy[arr_copy % 2 != 0] = -1
print("Odds replaced with -1:", arr_copy)

# 4. count divisible by 5
div5 = np.sum(arr % 5 == 0)
print("Count divisible by 5:", div5)
