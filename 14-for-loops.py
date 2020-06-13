# -- Python For Loops --

# + for loops
# The for loop does not require an indexing variable to set beforehand.
a_list = ['a', 'b', 'c', 'd']
print('1}} for loops: ', end='')
for i in a_list:
    print(i, ' ', end=' ')

# + Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
print("")
print("2}} Looping through a string 'banana': ", end='')
for i in 'Banana':
    print(i, ' ', end='')

print("")

# + The break Statement
a_list = ['a', 'b', 'c']
print('3}} break in for loops: ', end='')
for i in a_list:
    if i == 'b':
        break
    print(i, end=' ')

# + The continue Statement
print("")
print("4}} continue in for loops: ", end="")
for i in a_list:
    if i == 'b':
        continue
    print(i, end=' ')

print("")

# + The range() Function
#  To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.

print("5}} for loop by range():", end=' ')
# loop 5 time from 0 to 4
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

for i in range(5):
    print(i, end=' ')

print('')

# The range() function defaults to 0 as a starting value,
# however it is possible to specify the starting value by adding a parameter: range(2, 6),
# which means values from 2 to 6 (but not including 6):

print('6}} for loop in specific range:', end=' ')
# from 5 to 9
for i in range(5, 10):
    print(i, end=' ')

print("")

# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

print('7}} for loop in specific range and step:', end=' ')
# from 5 to 9
for i in range(10, 100, 10):
    print(i, end=' ')

print("")

# + Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
print("8}} else in for loops:", end=' ')
for i in a_list:
    print(i, end=' ')
else:
    print('Finally finish!')

# + Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
print("9}} Nested Loops:", end=" ")
for x in adj:
    for y in fruits:
        print(x, y, end=', ')
    print('')

# + The pass Statement
for x in [1, 2, 3]:
    pass

