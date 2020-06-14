# -- Python Math --
# Python has a set of built-in math functions, including an extensive math module,
# that allows you to perform mathematical tasks on numbers.

# + Built-in Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable:
a_list = [1, 2, 3, 4, 5]
print("min():", min(a_list))
print("max():", max(a_list))

# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print("abs(-7.25):", x)

# The pow(x, y) function returns the value of x to the power of y (xy).
x = pow(4, 3)
# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
print("pow(4, 3):", x)

# + The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.
# To use it, you must import the math module:

import math

x = math.sqrt(64)
print("math.sqrt(64):", x)

ceil_val = math.ceil(25.5)
floor_val = math.floor(25.5)

print("math.ceil(25.5):", ceil_val)
print("math.floor(25.5):", floor_val)

print("math.pi:", math.pi)

# + Complete Math Module Reference
# you will find a complete reference of all methods and constants that belongs to the Math module
# https://www.w3schools.com/python/module_math.asp

# https://www.w3schools.com/python/python_math.asp
