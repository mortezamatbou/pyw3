# -- Python String Formatting --
# To make sure a string will display as expected, we can format the result with the format() method.

# + String format()
# The format() method allows you to format selected parts of a string.
# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?
# To control such values, add placeholders (curly brackets {}) in the text,
# and run the values through the format() method:

price = 250
price_2 = 250.552
txt = "The price is {}"
txt_2 = "The price is {:.2f}"
print(txt.format(price))
print(txt_2.format(price_2))

# Check out all formatting types in https://www.w3schools.com/python/ref_string_format.asp

# + Multiple Values
# If you want to use more values, just add more values to the format() method:
txt_3 = "My name is {} from {}"
name = "More"
country = "USA"
print(txt_3.format(name, country))

# + Index Numbers
# You can use index numbers (a number inside the curly brackets {0})
# to be sure the values are placed in the correct placeholders:

txt_4 = "My name is {1} from {0}"
name = "Moree"
country = "Germany"
print(txt_4.format(country, name))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# + Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname},
# but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
txt_6 = "My name is {name} form {country}"
print(txt_6.format(country="Iran", name="More"))

# https://www.w3schools.com/python/python_string_formatting.asp
