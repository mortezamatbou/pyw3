# -- Python JSON --

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# + JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.
import json

# + Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# ::NOTE:: The result will be a <<Python dictionary>>

# some json
# json_text = "{'name': 'More', 'age': 25}"
json_text = '{"name": "More", "age": 25}'

# parse json_text
json_decode = json.loads(json_text)

print(json_decode)
print(json_decode['name'], json_decode['age'])

# + Convert from Python to JSON
# # a Python object (dict)
a_dict = dict(name="More", age=25)

# convert into JSON
json_encode = json.dumps(a_dict)

# the result is a JSON string:
print(json_encode)

# ::NOTE:: You can convert Python objects of the following types, into JSON strings:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
# dict  -> Object
# list  -> Array
# tuple -> Array
# str   -> String
# int   -> Number
# float -> Number
# True  -> true
# False -> false
# None  -> null

# Convert a Python object containing all the legal data types:
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

x_encode = json.dumps(x)

print(x_encode)

# + Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:
print(json.dumps(x, indent=2))

print(json.dumps(x, indent=2, separators=('. ', ' = ')))

# + Order the Result
# The json.dumps() method has parameters to order the keys in the result:
# Use the sort_keys parameter to specify if the result should be sorted or not:
print(json.dumps(x, indent=2, sort_keys=True))

# https://www.w3schools.com/python/python_json.asp
