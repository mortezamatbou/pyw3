import numpy as np

# By default, Python have these data types:
"""
strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
"""

# Data Types in NumPy: NumPy has some extra data types. i for integers, u for unsigned integers etc
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

arr = np.array([1.5, 2, 3, 4, 5])
print(arr.dtype)

arr = np.array(['Name 1', 'Name 2', 'Name 3'])
print(arr.dtype)

# --- Creating Arrays With a Defined Data Type ---
arr = np.array(object=[1, 1.5, 2, 3, 4], dtype='i')
print(arr, arr.dtype)

arr = np.array(object=["1", 1.5, 2, 3, 4], dtype='S')
print(arr, arr.dtype)

# --- For i, u, f, S and U we can define size as well. ---
arr = np.array([1, 2, 3, 4, 5], dtype='i4')
print(arr, arr.dtype)

# --- What if a Value Can Not Be Converted ??? ---
# If a type is given in which elements can't be casted then NumPy will raise a ValueError.
# Example: A non integer string like 'a' can not be converted to integer (will raise an error):

# arr = np.array(['a', '2', '3'], dtype='i')

# --- Converting Data Type on Existing Arrays ---
arr = np.array([1.5, 1.2, 1.1])
print(arr, arr.dtype)
# return new ndarray
arr = arr.astype('i')
print(arr, arr.dtype)

# change datatype from integer to boolean
arr = np.array([1, 1.5, 0, 30, -1])
print(arr, arr.dtype)
arr = arr.astype(bool)
print(arr, arr.dtype)
arr = np.array([1, 1.5, 0, 30, -1], dtype=bool)
print(arr, arr.dtype)
