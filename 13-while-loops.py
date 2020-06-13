# -- Python While Loops --

# + Python Loops
# Python has two primitive loop commands:
# while
# for

# + The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
print("1]] While loops: ", end='')
while i < 10:
    print(i, " ", end='')
    i += 1

print("")

# + The break Statement
# With the break statement we can stop the loop even if the while condition is true:
i = 1

print("2]] break in while: ", end='')
while i < 5:
    print(i, " ", end='')
    if i == 3:
        break;
    i += 1

print("")

# + The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
i = 1
print("3]] continue in while: ", end='')
while i < 10:
    print(i, ' ', end='')
    if i == 5:
        i += 1
        continue
    i += 1

print("")

# + The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
print("4]] else in while loops:", end=" ")
while i < 5:
    print(i, " ", end="")
    i += 1
else:
    print("i is no longer less than 5")

# https://www.w3schools.com/python/python_while_loops.asp
