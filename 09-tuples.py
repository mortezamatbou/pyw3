# -- Tuples in Python --
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# + Create a tuple
a_tuple = ("t0", "t1", "t2", "t3", "t4", "t5", "t6")
print("1] Make a tuple:", a_tuple)

# + Access Tuple Items
print("2] Access to tuple item:", a_tuple[0])

# + Negative Indexing
print("3] Negative indexing", a_tuple[-1])

# + Range of Indexes
# Note: The search will start at index 0 (included) and end at index 3 (not included).
print("4] Range of indexes:", a_tuple[0:3])

# + Range of Negative Indexes
# This example returns the items from index -4 (included) to index -1 (excluded)
print("5] Range of negative indexes", a_tuple[-4:-1])

# + Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are <unchangeable>, or <immutable> as it also is called.
# But there is a workaround.
# You can convert the tuple into a list, change the list
# and convert the list back into a tuple.

a_tuple = tuple(("v2", "v2", "v3"))
tuple_to_list = list(a_tuple)
tuple_to_list.append('v4')
tuple_to_list[0] = 'v1'
tuple_to_list.insert(0, 'v0')
a_tuple = tuple(tuple_to_list)  # ('v0', 'v1', 'v2', 'v4')
print("6] Change tuple value:", a_tuple)

# + Loop Through a Tuple
print("7] Loop in tuple:", end=" ")
for item in a_tuple:
    print(item, end=" | ")

print("")

if 'v1' in a_tuple:
    print("8] item = 'v1' is in a_tuple:")
else:
    print("8] item = 'v1' is not in a_tuple:")

# + Length of Tuple
print("9] a_tuple Length:", len(a_tuple))

# a_tuple[3] = "orange" # This will raise an error
# print(a_tuple)

# + Create Tuple With One Item
a_tuple_2 = ("v0",)
print("10] Make a tuple with one item:", type(a_tuple_2))

a_tuple_2 = ("v0")  # NOT a tuple
print("11] Make a tuple with one item [NOT A TUPLE]:", type(a_tuple_2))

# + Remove Items
# ::NOTE:: <<<You cannot remove items in a tuple>>> ::NOTE::
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:

# + Remove tuple completely
del a_tuple_2
# print(a_tuple_2)  # This will raise an error because the tuple no longer exists

# + Join Two Tuples
tuple_1 = ('v0', 'v1')
tuple_2 = tuple(('v2',))

tuple_3 = tuple_1 + tuple_2
print("12] Join Two tuple:", tuple_3)

# + The tuple() Constructor
# Using the tuple() method to make a tuple:
a_tuple_1 = tuple(("v1",))
a_tuple_2 = tuple(("v1", "v2"))
print("13] Make by tuple():", a_tuple_1, a_tuple_2)

# https://www.w3schools.com/python/python_tuples.asp
