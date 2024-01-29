import numpy as np

# Slicing in python means taking elements from one given index to another given index.

# We pass slice instead of index like this: [start:end].
# If we don't pass start its considered 0
# We can also define the step, like this: [start:end:step].
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Note: The result includes the start index, but excludes the end index
print(arr[1:3])
print(arr[3:])
