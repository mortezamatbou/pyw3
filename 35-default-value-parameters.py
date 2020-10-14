# -- Default values for parameters --

accounts = {
    'checking': 1958.00,
    'saving': 3952.02
}

print("1] accounts:", accounts)


def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balance"""
    accounts[name] += amount
    return accounts[name]


add_balance(2)
print("2] accounts:", accounts)
