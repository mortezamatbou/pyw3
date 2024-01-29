import numpy as np

# --- The Difference Between Copy and View
"""
-- [copy] is a new array
------ The copy owns the data and any changes made to the copy will not affect original array

-- [view] is just a view of the original array
------ any changes made to the original array will not affect the copy
"""

# The copy SHOULD NOT be affected by the changes made to the original array.
arr = np.array([10, 20, 30, 40])
copy = arr.copy()
print(arr)
print(copy)
copy[0] += 1
arr[0] -= 1
print(arr)
print(copy)

del arr, copy

# --- Make Changes in the VIEW ---
arr = np.array([10, 20, 30, 40])
# The original array SHOULD be affected by the changes made to the view.
copy = arr.view()
copy[0] = 0
print(arr)
print(copy)

del arr, copy
# --- Check if Array Owns its Data ---
""" 
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
Every NumPy array has the attribute ''base'' that returns ''None'' if the array ''owns the data''.
Otherwise, the base attribute refers to the original object.
"""

arr = np.array([1, 2, 3, 4, 5])

copy = arr.copy()
view = arr.view()

"""
The copy returns None.
The view returns the original array.
"""
print(copy.base, view.base)
