# -- Python RegEx --
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# + RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x != None:
    print(x.string)

x = re.findall("More", txt)
print(x)
x = re.findall("ai", txt)
print(x)

# + The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
x = re.search("Spain", txt)
# ::NOTE:: If no matches are found, the value None is returned:
print(x.start())

# + The split() Function
# The split() function returns a list where the string has been split at each match:

x = re.split("\s", txt)
print(x)

# You can control the number of occurrences by specifying the maxsplit parameter:
txt_2 = "a,b,c,d,e"
x = re.split(",", txt_2, 2)
print(x)
x = re.split(",", txt_2)
print(x)

# + The sub() Function
# The sub() function replaces the matches with the text of your choice:
slug_txt = "whats php"
x = re.sub("\s", "-", slug_txt)
print(x)

# You can control the number of replacements by specifying the count parameter:
slug_txt = "what is php"
x = re.sub("\s", "-", slug_txt, 1)
print(x)

# + Match Object
# A Match Object is an object containing information about the search and the result.
# ::NOTE:: If there is no match, the value None will be returned, instead of the Match Object.

txt = "The rain in Spain"

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", txt)

# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
print(x.span())
print(x.string)
print(x.group())

# ::NOTE:: If there is no match, the value None will be returned, instead of the Match Object.

# https://www.w3schools.com/python/python_regex.asp
