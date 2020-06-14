# -- Python Datetime --
# A date in Python is not a data type of its own,
# but we can import a module named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)

# + Date Output
# When we execute the code from the example above the result will be:
#  2020-06-14 15:39:47.716133
# The date contains year, month, day, hour, minute, second, and microsecond.

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# + Creating Date Objects
x = datetime.datetime(1992, 2, 14)
print(x)
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone),
# but they are optional, and has a default value of 0, (None for timezone).

# + The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

x = datetime.datetime(2020, 2, 7)
print(x.strftime("%B"))

# https://www.w3schools.com/python/python_datetime.asp
