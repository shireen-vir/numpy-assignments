import numpy as np

# Q4 - random numbers and basic stats

# 1. 100 random numbers between 0 and 1
data = np.random.rand(100)
print("First 10 values:", data[:10])

# 2. stats
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std dev:", np.std(data))

# 3. count values > 0.5
count = np.sum(data > 0.5)
print("Values greater than 0.5:", count)

# 4. normalize between 0 and 1
# formula: (x - min) / (max - min)
normalized = (data - data.min()) / (data.max() - data.min())
print("Normalized - min:", normalized.min(), "max:", normalized.max())
