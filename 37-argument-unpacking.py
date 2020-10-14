# -- Argument unpacking --

accounts = {
    'checking': 1523.25,
    'savings': 1542.22
}


def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balance"""
    accounts[name] += amount
    return accounts[name]


transactions = [
    (-180.2, 'checking'),
    (156.50, 'savings'),
    (-98.23, 'checking'),
    (52.63, 'savings'),
    (52.63, 'savings'),
    (-75.63, 'checking'),
]

for x in transactions:
    # this is called argument unpacking and this asterisk
    # here is unpacking operator
    # that we can use to unpack any iterable into arguments
    add_balance(*x)  # equal -> add_balance(x[0], x[1])

# + name of argument
# in any function call in python, you can specify the name of the parameter
# that just makes the function call a bit more readable
add_balance(amount=152.36, name='checking')

for x in transactions:
    amount, name = x
    add_balance(amount, name)

    # this can be pretty useful cause now you know that x[0] whatever that is,
    # is going to the amount property
    # A benefit of these named arguments is that
    # you can put theme in any order you want
    add_balance(name=x[1], amount=x[0])


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


# imagine these users are coming from a database
users = [
    {'username': 'Mori', 'password': '321'},
    {'username': 'Ali', 'password': '123'}
]

# we've mapped over the User.from_dict method for the users list
# so that calls it from dict method for each user
# passing the dictionary to method
# and then we were able to create a new User from each dictionary

# now that we have argument unpacking
user_objects = map(User.from_dict, users)
user_objects_2 = [User.from_dict(u) for u in users]


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password


# We are iterable over users
# too many usernames in here
user_objects_3 = [User(username=u['username'], password=u['password']) for u in users]

# There must be a better way and there is
user_objects_4 = [User(**data) for data in users]


# double asterisk and what this does
# is that this is a dictionary unpacking
# it unpacks a dictionary as named arguments

# it is important because dictionary may not be in order
