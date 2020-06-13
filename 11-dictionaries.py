# -- Python Dictionaries --
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.

# + Create a Dictionary in python
a_dict = {'first_name': "More", "last_name": 'More Than', "age": 28}
print("1}} Create a Dictionary:", a_dict)

# + Accessing Items
print("2}} Accessing items:", a_dict['first_name'], a_dict['last_name'], a_dict['age'])

# There is also a method called get() that will give you the same result:
print("3}} Accessing to dictionary items with get():", a_dict.get('first_name'))

# + Change Values
a_dict['first_name'] = "Mori"
a_dict['last_name'] = "Mori Than"
a_dict['age'] = 27
print("4}} Change value of dictionary", a_dict)

# + Loop Through a Dictionary

print("5}} Dictionary Loop: ", end="")
for x in a_dict:
    print(a_dict[x], end=' ')

print("")
print("6}} Use values() method to return value [LOOP]: ", end="")
# + You can also use the values() method to return values of a dictionary:
for x in a_dict.values():
    print(x, end=" ")

print("")

print("7}} Use values() method to return value [LOOP]: ", end="")
# + You can also use the values() method to return values of a dictionary:
for x in a_dict.values():
    print(x, end=" ")

print("")

# + Check if Key Exists
if 'first_name' in a_dict:
    print("8}} first_name is in a_dict")
else:
    print("8}} first_name is not in a_dict")

# + Dictionary Length
# To determine how many items (key-value pairs) a dictionary has, use the len() function.
print("9}} Length of a_dic:", len(a_dict))

# + Adding Items
a_dict['new_field'] = 'new_field_value'
print("10}} Adding item to dictionary:", a_dict)

# + Removing Items
# There are several methods to remove items from a dictionary
dict_1 = {
    'name': 'More',
    'family': "Than",
    'field': 'IT',
    'other_field': 'other_field_value'
}
dict_1.pop('other_field')
print("11}} Remove items by pop():", dict_1)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
dict_1['other_field'] = 'New Value'
dict_1.popitem()  # pop last inserted item
print("12}} Remove last inserted item by popitem():", dict_1)

# The <del> keyword removes the item with the specified key name:
del dict_1
# print(dict_1)  # This will cause an error because dict_1 no longer exists.

# The clear() method empties the dictionary
dict_1 = {"name": "More", "field": "IT", "age": 28}
print("13}} empty an dictionary with clear(): [dict_1] ->", dict_1)
dict_1.clear()
print("dict_1 is empty after use clear(): [dict_1] ->", dict_1)

# + Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1,
# because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

dict_1 = {"a": "a_value", 'b': 'b_value', 'c': 'c_value'}
dict_2 = {"d": "d_value", 'e': 'e_value', 'f': 'f_value'}

# There are ways to make a copy, one way is to use the built-in Dictionary method copy()
copied_dict = dict_1.copy()
print("14}} Copy a Dictionary:", copied_dict)

# Another way to make a copy is to use the built-in function dict()
copied_dict = dict(dict_2)
print("15}} Copy a Dictionary with dict():", copied_dict)

# Nested Dictionaries
# A dictionary can also contain many dictionaries, this is called nested dictionaries.
nested_dict = {
    "user_1": {
        "name": "More",
        'year': 1992
    },
    "user_2": {
        'name': "Mori",
        'year': 1991
    },
    "user_3": {
        'name': 'Moriel',
        'year': 1990
    }
}

nested_dict_2 = {
    "post_1": {
        'title': "What's python",
        'category': {
            'id': 35,
            'title': 'python'
        }
    },
    "post_2": {
        'title': "What's PHP",
        'category': {
            'id': 34,
            'title': 'php'
        }
    }
}

# + The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary:
a_dict = dict(name="Mori", family="More", age=28, another_dict={'a': 'a_value', 'b': 'b_value'})
# ::NOTE:: That keywords are not string literals
# ::NOTE:: The use of equals rather than colon for the assignment
print("16}} Make a dictionary with dict() constructor:", a_dict)

# https://www.w3schools.com/python/python_dictionaries.asp
