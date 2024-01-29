import numpy as np

# ------ Array Indexing
# Array indexing is the same as accessing an array element.

arr = np.array([1, 2, 3, 4])
print(arr[0], arr[3])

# Access 2-D arrays
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr[0][0], arr[0][1])  # print 1 and 2
# print(arr[0, 0], arr[0, 1])  # print 1 and 2

# print(arr[1][0], arr[1][3])  # print 5 and 8
# print(arr[1, 0], arr[1, 3])  # print 5 and 8

arr = np.array([  # 1-D
    [  # 2-D
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ],
    [  # 3-D
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
])
# print(arr[0, 0, 0], arr[0][0][0], arr[0][0, 0], arr[0, 0][0])
# print(arr[0])
# print(type(arr[0]))
# print(type(arr[0, 0, 0]))

# Negative Indexing
print(arr[0, 0, -1], arr[0][0][-1], arr[0][0, -1], arr[0, 0][-1])
