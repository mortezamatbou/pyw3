import numpy as np

# --- Joining NumPy Arrays ---
'''
Joining means putting contents of two or more arrays in a single array.
In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis.
If axis is not explicitly passed, it is taken as 0.
'''

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2, [1, 2, 3]))
print(arr)

del arr1, arr2, arr

# --- Join two 2-D arrays along rows (axis=1)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

del arr1, arr2, arr

# --- Joining Arrays Using Stack Functions ---
'''
Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other,
ie. stacking.
We pass a sequence of arrays that we want to join to the stack() method along with the axis.
If axis is not explicitly passed it is taken as 0.
'''
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

del arr, arr1, arr2

# --- Stacking Along Rows ----
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(np.hstack((arr1, arr2)))

# --- Stacking Along Columns ----
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 11, 12])
print(np.vstack((arr1, arr2)))

# --- Stacking Along Height (depth) ---
arr1 = np.array([1, 2, 3])
arr2 = np.array([10, 11, 12])
print(np.dstack((arr1, arr2)))

arr1 = np.array([[1, 2], [3, 4], [5, 6]])
arr2 = np.array([[7, 8], [9, 10], [11, 12]])
print(np.dstack((arr1, arr2)))

print('--------------*******')

for i in np.dstack((arr1, arr2)):
    print(i)
    print('-------------')

