import numpy as np

# ------ Intro

# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method,
# and it will be converted into an ndarray

# list as ndarray
data = [10, 50, 60, 15]
# set as ndarray
data2 = {1, 2, 3}

arr = np.array(data)
print(arr)
print(type(arr))

del arr, data, data2

# Dimensions in arrays

# 0-D array
arr = np.array(40)
print(arr)
print(type(arr))

# 1-D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2-D array
data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]
arr = np.array(data)
print(arr)

# 3-D array
data = [  # 1-D
    [  # 2-D
        [1, 2, 3],  # 3-D
        [4, 5, 6]
    ],
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
]
arr = np.array(data)
# ndim attribute that returns an integer that tells us how many dimensions the array have
print(arr.ndim)  # print 3

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
