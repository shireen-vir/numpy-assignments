import numpy as np

# Q5 - math operations on arrays

# 1. two arrays of size 10
a = np.random.randint(1, 20, size=10)
b = np.random.randint(1, 20, size=10)
print("a:", a)
print("b:", b)

# 2. basic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 3. sqrt, square, exp
print("Square root of a:", np.sqrt(a))
print("Square of a:", np.square(a))
print("Exponential of a:", np.exp(a))
