# -- Python if...else --
# Python Conditions and If statements

# Python supports the usual logical conditions from mathematics:
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# ::NOTE:: These conditions can be used in several ways, most commonly in "if statements" and loops.

a = 20
b = 10

if a > b:
    print("01- if statement. a Greater than b:", 'a=', a, 'b=', b)
else:
    print("01- if statement. a is not Greater than b:", 'a=', a, 'b=', b)

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# + Nested If and The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
if b > a:
    pass
elif a == b:
    pass
else:
    print("else")

# + Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

if a > b: print("a is greater than b")

# + Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
# This technique is known as Ternary Operators, or Conditional Expressions.

a = 2
b = 330
print("A") if a > b else print("B")

# You can also have multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# top command can rewrite
if b < a < c:
    print("Both conditions are True")

# Or
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# https://www.w3schools.com/python/python_conditions.asp
