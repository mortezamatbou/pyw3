import numpy as np

# --- Shape of an array ---
# The shape of an array is the number of elements in each dimension.

# --- Get the shape of an array ---
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# shape attribute return a tuple with each index having the number of corresponding elements
print(arr.shape)

arr = np.array([1, 2, 3], ndmin=5)
print(arr.shape)

# --- What does the shape tuple represent?
"""
Integers at every index tells about the number of elements the corresponding dimension has.
In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.
"""

# --- Reshaping arrays
"""
Reshaping means changing the shape of an array.
The shape of an array is the number of elements in each dimension.
By reshaping we can add or remove dimensions or change number of elements in each dimension.
"""

print("--------------------------- reshape -------------------------------")
# --- Reshape From 1-D to 2-D ---
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# reshape method return new array
print(arr, arr.shape)
arr_reshape = arr.reshape(3, 4)
print(arr_reshape, arr_reshape.shape)
arr_reshape = arr.reshape(2, 6)
print(arr_reshape, arr_reshape.shape)

del arr, arr_reshape
# --- Reshape From 1-D to 3-D ---

arr = np.array([1, 2, 3, 4, 5, 6])
arr_reshape = arr.reshape(3, 2, 1)
print(arr_reshape)

a = [
    [
        [1], [2]
    ],
    [
        [3], [4]
    ],
    [
        [5], [6]
    ]
]
a = np.array(a)
print(a.shape)

del arr, arr_reshape

# --- Can We Reshape Into any Shape ??? ---
"""
Yes, as long as the elements required for reshaping are equal in both shapes.
We can reshape an 8 elements 1D array
 -- into 4 elements in 2 rows 2D array
 -- but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.
"""

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# We cannot reshape it into 3x3
# arr.reshape(3, 3)  # Will raise error
arr_reshape = arr.reshape(4, 2)
print(arr_reshape, arr_reshape.shape, arr_reshape.base, arr.base)

del arr, arr_reshape

print('------------------------ COPY OR VIEW ------------------')
# --- Returns Copy or View ??? ---

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.base, arr.reshape(2, 3), arr.reshape(2, 3).base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr_reshape = arr.reshape(2, 2, -1)
print(arr_reshape)

a = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

del a, arr_reshape, arr

# --- Flattening the arrays ---
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr, arr.shape)
arr = arr.reshape(-1)
print(arr, arr.shape)

"""
Note: There are a lot of functions for changing the shapes of arrays in numpy flatten,
ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc.
These fall under Intermediate to Advanced section of numpy.
"""
