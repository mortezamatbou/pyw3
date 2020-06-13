# -- Python Lists --
# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# 1- List: is a collection which is ordered and changeable. Allows duplicate members.
# 2- Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
# 3- Set: is a collection which is unordered and unindexed. No duplicate members.
# 4- Dictionary: is a collection which is unordered, changeable and indexed. No duplicate members.

# -| List |-
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
a_list = ['apple', 'apple', 'orange', 'cherry']
print("01) a_list:", a_list)

# + Access to item
print("02) Item of a_list:", a_list[0])

# + Get count of a list
print("03) Count of a_list:", len(a_list))

# + Negative indexing:
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc
print("04) Negative indexing:", a_list[-1])  # print last item of a_list

# + Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# Remember that the first item has index 0.
print("05) Range of Indexes:", a_list[2:])  # [start:end] [:1] [1:] [2:4]

# + Range of Negative Indexes
# This example returns the items from index -3 (included) to index -1 (excluded)
print("06) Range of negative indexes:", a_list[-3:-1])

# + Change Item Value
a_list[0] = 'banana'
print("07) Change item value:", a_list)

# + Loop Through a List
print("08) Loop a List:", end=" ")
for item in a_list:
    print(item, end="|")
print('')

# + Check if Item Exists

if 'banana' in a_list:
    print("09) banana is in a_list")
else:
    print("09) banana is not in a_list")

# + List Length
print("10) Length of a_list:", len(a_list))

# + Add Items: To add an item to the end of the list, use the append() method
new_list = ['one', 'two', 'three']
new_list.append('four')
print("11) Add items to list:", new_list)

# To add an item at the specified index, use the insert() method
new_list.insert(0, 'zero')
print("12) Add items to list:", new_list)

# + Remove item
new_list_2 = ['a', 'b', 'c', 'd', 'a']
new_list_2.remove('a')
new_list_2.remove('a')
print("13) Remove item from list:", new_list_2)

# + pop list
new_list_3 = ['a', 'b', 'c', 'd']
new_list_3.pop()
new_list_3.pop(0)
new_list_3.pop(1)
print("14) Pop list:", new_list_3)

# + Delete specified index of list
new_list_4 = ['a', 'b', 'c', 'd']
del new_list_4[len(new_list_4) - 1]
print("15) Remove By del keywords:", new_list_4)
# The del keyword can also delete the list completely
del new_list_4
# print("16) Remove By del completely:", new_list_4)  # name 'new_list_4' is not defined

# + Empty List
new_list_5 = ['a', 'b']
new_list_5.clear()
print("17) Empty List (new_list_5):", new_list_5)

# + Copy a List
list_1 = ['a', 'b', 'c', 'd']
list_1_copy = list_1.copy()
list_1_copy.pop()
print("18) List copy (this list is a copy of list_1):", list_1, list_1_copy)
# Another way to make a copy is to use the built-in method list().
list_1_copy_2 = list(list_1)
print("19) Another way to copy a list:", list_1, list_1_copy_2)

# + Join Two Lists
# One of the easiest ways are by using the + operator.
list_join_1 = ['a', 'b', 'c']
list_join_2 = ['d', 'e', 'f']
joined_list = list_join_1 + list_join_2
print("20) Join Two list:", joined_list)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:
list_join_3 = ['a', 'b', 'c']
list_join_3.extend(list_join_2)
print("21) Join Two list by extends function:", list_join_3)

# + The list() Constructor: It is also possible to use the list() constructor to make a new list
a_list_2 = list(("d", "a", "c", "b", "a", "e"))  # note the double round-brackets
print("22) Make new list by list():", a_list_2)
print("23) Count of 'a' in a_list_2:", a_list_2.count('a'))
a_list_2.reverse()
print("24) Reverse a_list_2:", a_list_2)
a_list_2.sort()
print("25) Sort a_list_2:", a_list_2)

# https://www.w3schools.com/python/python_lists.asp
