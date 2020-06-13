# -- Python Lambda --
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# + Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:
# A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a: a + 10

print(x(2))

# Lambda functions can take any number of arguments:
x2 = lambda a, b: a + b
print(x2(10, 2))


# + Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:

def myfunc(n):
    return lambda a: a * n


lambda_1 = myfunc(2)
lambda_2 = myfunc(4)

print(lambda_1(2))
print(lambda_2(2))

# ::NOTE:: Use lambda functions when an anonymous function is required for a short period of time.

# https://www.w3schools.com/python/python_lambda.asp
