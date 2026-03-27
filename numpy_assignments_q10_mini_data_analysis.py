import numpy as np

# Q10 - mini data analysis project

np.random.seed(42)  # for reproducibility

# 1. dataset: 50 students, 5 subjects, marks out of 100
marks = np.random.randint(30, 101, size=(50, 5))
print("Marks dataset shape:", marks.shape)

# 2. total and average marks per student
total_marks = np.sum(marks, axis=1)
avg_marks = np.mean(marks, axis=1)
print("Total marks (first 5 students):", total_marks[:5])
print("Average marks (first 5 students):", avg_marks[:5])

# 3. topper and students above 75%
topper_idx = np.argmax(total_marks)
print("Topper is student index:", topper_idx)
print("Topper's total marks:", total_marks[topper_idx])

# 75% of max total (5 subjects * 100 = 500)
above_75 = np.sum(total_marks > 375)
print("Students scoring above 75%:", above_75)

# 4. normalize the dataset
marks_norm = (marks - marks.min()) / (marks.max() - marks.min())
print("Normalized marks - min:", marks_norm.min(), "max:", marks_norm.max())
