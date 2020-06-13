# -- Operators in python --

# - Type of operators:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

x = 20
y = 10

# - Arithmetic operators:
# + - * /  % ** //
print("01:", x + y)  # Addition
print("02:", x - y)  # Subtraction
print("03:", x * y)  # Multiplication
print("04:", x / y)  # Division
print("05:", x % y)  # Modulus
print("06:", x ** y)  # Exponentiation
print("07:", x // y)  # Floor division

# - Assignment Operators
xx = 255
print("08:", xx)

xx += 5  # xx -> 260
print("09:", xx)
xx -= 5  # xx -> 255
print("10:", xx)

xx *= 5  # xx = 255 * 5 -> 1275
print("11:", xx)
xx /= 5  # xx = 505 / 5 -> 255.0 -> return value in float
print("12:", int(xx))  # Type cast to int 255.0 to 255

xx %= 5  # xx = xx % 5 -> 0.0
print("13:", xx)

# ----- Reset xx to 255 -----
xx = 255  # -----------------
# ---------------------------

xx //= 5  # xx = xx // 5
print("14:", xx)

# ----- Reset xx to 255 -----
xx = 255  # -----------------
# ---------------------------

xx **= 2  # xx = xx ** 2
print("15:", xx)  # 65025

# ----- Reset xx to 255 -----
xx = 255  # -----------------
# ---------------------------
xx &= 2  # x = xx & 2
print("16:", xx)

# ----- Reset xx to 255 -----
xx = 255  # -----------------
# ---------------------------
xx |= 256  # xx = xx | 255
print("17:", xx)

# ----- Reset xx to 255 -----
xx = 255  # -----------------
# ---------------------------
xx ^= 2  # xx = xx ^ 2
print("18:", xx)

# ----- Reset xx to 256 -----
xx = 256  # -----------------
# ---------------------------
xx >>= 1  # xx = xx >> 1
print("19:", xx)  # 128

# ----- Reset xx to 256 -----
xx = 256  # -----------------
# ---------------------------
xx <<= 1  # xx = xx << 1
print("20:", xx)  # 512

# - Python Comparison Operators. Comparison operators are used to compare two values
k = 20
j = 10

print("21:", k == j)
print("22:", k > j)
print("23:", k != j)
print("24:", k >= 20)
print("25:", j <= 10)

# - Python Logical Operators. Logical operators are used to combine conditional statements
# and, or, not
r = k > 1 and k < 20  # equal to: 1 < k < 21 -> return False
# r = 1 < k < 21  #  return True
print("26:", r)

r = k > 3 or k <= 20
print("27:", r)

# returns False because not is used to reverse the result
r = not (k > 0 and k < 21)  # Actual result is True. this will reverse
print("28:", r)

# - Python Identity Operators
# is: Returns True if both variables are the same object -> o is l
# is not: Returns True if both variables are not the same object -> o is not l

o = ["apple", "banana"]
l = ["apple", "banana"]
n = o

# returns True because n is the same object as o
print("29:", o is n)
print("30:", o is not n)

# returns False because o is not the same object as l, even if they have the same content
print("31:", o is l)
print("32:", o is not l)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because o is equal to l
print("33:", o == l)

# - Python Membership Operators. Membership operators are used to test if a sequence is presented in an object
list_1 = ["apple", "banana"]

# returns True because a sequence with the value "banana" is in the list
print("34:", "banana" in list_1)
print("35:", "pineapple" not in list_1)

# - Python Bitwise Operators. Bitwise operators are used to compare (binary) numbers
# & AND -> Sets each bit to 1 if both bits are 1
# | OR -> Sets each bit to 1 if one of two bits is 1
# ^ XOR -> Sets each bit to 1 if only one of two bits is 1
# ~ NOT -> Inverts all the bits
# << Zero fill left shift -> Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> Singed right shift -> Shift right by pushing copies of the leftmost bit in from the left
# and let the rightmost bits fall off

# https://www.w3schools.com/python/python_operators.asp
