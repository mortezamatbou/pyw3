import numpy as np

arr = np.array([1, 2, 3])
for i in arr:
    print(i)

# --- Iterating 2-D Arrays ---

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

for row in arr.reshape(2, 4):
    print(row)

for row in arr.reshape(2, 4):
    for i in row:
        print(i, end=' ')
    print('')

# --- Iterating 3-D Arrays ---
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr = arr.reshape(3, 2, 2)

a = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ],
    [
        [9, 10],
        [11, 12]
    ]
]

print("\n--------------------")
for level_1 in arr:
    for level_2 in level_1:
        for element in level_2:
            print(element, end=' ')
    print("\n--------------------")

del arr
# --- Iterating Arrays Using nditer()
"""
The function nditer() is a helping function that can be used from very basic to very advanced iterations.
It solves some basic issues which we face in iteration
"""
"""
In basic for loops,
iterating through each scalar of an array we need to use n for loops which
can be difficult to write for arrays with very high dimensionality.
"""
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

for x in np.nditer(arr):
    print(x, end=' ')
print("\n")

# --- Iterating Array With Different Data Types ---
"""
We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
NumPy does not change the data type of the element in-place (where the element is in array)
so it needs some other space to perform this action,
that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].
"""

arr = np.array([1.5, 2.5, 33.5, 31.2])
for i in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(i, end=' ')

print("\n")

# --- Iterating With Different Step Size ---
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Iterate through every scalar element of the 2D array skipping 1 element
for x in np.nditer(arr[:, ::2]):
    print(x, end=' ')
print('')

# --- Enumerated Iteration Using ndenumerate() ---
'''
Enumeration means mentioning sequence number of somethings one by one.
Sometimes we require corresponding index of the element while iterating,
the ndenumerate() method can be used for those usecases.
'''

arr = np.array([[1, 2, 3], [4, 5, 6]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
