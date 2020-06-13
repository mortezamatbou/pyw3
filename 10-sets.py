# -- Sets in Python --
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets

# + Make a set
# ::NOTE:: Sets are unordered, so you cannot be sure in which order the items will appear.

a_set = {"one", "two", "three", "four", "five", "six"}
print("1} Sets in python:", a_set)

# + Access Items
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop,
# or ask if a specified value is present in a set, by using the in keyword.

print("2} Loop a set: ", end="")
for item in a_set:
    print(item, end=" | ")

print("")

# + Change Items
# ::NOTE:: Once a set is created, you cannot change its items, but you can add new items.


# + Add Items
# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.
a_set.add('six')  # this will not added to set, because we have six in a_set
print("3} Add item to set:", a_set)

a_set.update(['seven', 'eight', 'nine', 'ten'])
print("4} Add multiple items to a set:", a_set)

# + Get the Length of a set
print("5} Get length of a set:", len(a_set))

# + Remove item
# To remove an item in a set, use the remove(), or the discard() method.
# ::NOTE:: If the item to remove does not exist, remove() will raise an error.
# a_set.remove('zero')  # This will raise an error
a_set.remove('one')
print("6} Get length of a set:", len(a_set))

# Remove item with discard function
# ::Note:: If the item to remove does not exist, discard() will NOT raise an error.
a_set.discard('one')
a_set.discard('two')
print("7} Get length of a set:", len(a_set))

# + Pop a set
# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.

# ::NOTE:: The return value of the pop() method is the removed item.
# ::NOTE:: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
poped_item = a_set.pop()
print("8} POP item from set:", len(a_set), ' Pop value:', poped_item)

# + Clear a set
a_set.clear()
# del a_set  # Delete set completely
print("9} clear set:", a_set)

# + Join Two Sets
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another:

# ::NOTE:: Both union() and update() will exclude any duplicate items.

set_1 = {"a", "b", "c"}
set_2 = {"d", "b", "c", "e"}
set_1.update(set_2)
print("10} Join two set:", set_1)

# with union()
set_1 = {"a", "b", "c"}
set_2 = {"d", "b", "c", "e"}
joined_set = set_1.union(set_2)
print("11} Join two set with union():", joined_set)

# + The set() Constructor
a_set = set(('a', 'b', 'c'))  # note the double round-brackets
print("12} Make a set with set():", joined_set)

# https://www.w3schools.com/python/python_sets.asp
