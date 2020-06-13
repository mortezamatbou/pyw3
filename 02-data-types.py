# -- Data types in Python --

# Numeric Types: int, float, complex
int_var = 12
int_var_ = int(12)
float_var = 10.25
float_var_ = float(10.25)
complex_var = 1j
complex_var_ = complex(1j)

# Text Types: str
str_var = "Text var"
str_var_ = str("Text var")

# Sequence Types: list, tuple, range
list_var = ['A', 'B', 'C', 'D']
list_var_ = list(['A', 'B', 'C', 'D'])
tuple_var = ('A', 'B', 'C')
tuple_var_ = tuple(('A', 'B', 'C'))
range_var = range(5)

# Mapping Types: dict
dict_var = {"name": "More", "age": 28}
dict_var_ = dict(name="More", age=28)

# Set Types: set, frozenset
set_var = {'More', 'More than', 'More that'}
set_var_ = set(('More', 'More than', 'More that'))
frozenset_var = frozenset({'More', 'More than', 'More that'})

# Boolean Types: bool
boolean_var = True
boolean_var_ = bool(True)
boolean_var_2 = False
boolean_var_2_ = bool(False)

# Binary Types: bytes, bytearray, memoryview
bytes_var = b"More"
bytearray_var = bytearray(5)
memoryview_var = memoryview(bytearray(5))

print(type(str_var))

# https://www.w3schools.com/python/python_datatypes.asp
