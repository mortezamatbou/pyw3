# -- Mutable default argument --
# bad idea


def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)

    return {
        'name': name,
        'holder': holder,
        'account_holders': account_holders
    }


a1 = create_account("checking", "Mori")
print(a1)

a2 = create_account("savings", "Ali")
print(a2)

print(a1['account_holders'])
print(a2['account_holders'])

account_holders_2 = ["_Mori_", "_Ali_"]
a3 = create_account("savings", "Mori", account_holders_2)
print(a3)

a4 = create_account("checking", "Ali")
print(a4)


# Two ways to solve this problem

# first, not have a default argument
def create_account_2(name: str, holder: str, account_holders: list):
    account_holders.append(holder)
    return {
        'name': name,
        'holder': holder,
        'account_holders': account_holders
    }


# holders_account going to be empty every time
u1 = create_account_2("savings", "Mori__", [])
print(u1)

u2 = create_account_2("checking", "Ali__", [])
print(u2)


# two way
def create_account_3(name: str, holder: str, account_holders=None):
    if not account_holders:
        account_holders = []
    account_holders.append(holder)
    return {
        'name': name,
        'holder': holder,
        'account_holders': account_holders
    }


o1 = create_account_3("saving", 'Mori_-_', [])
print(o1)

o2 = create_account_3("checking", "Ali_-_", o1['account_holders'])
print(o2)

o3 = create_account_3("checking", "Rahim_-_")
print(o3)


class Test:

    def __init__(self, title):
        self.title = title


obj = Test("Title of class")
print("[[A]]", id(obj), obj.title)


def change_object_title(target_obj, new_title):
    print("[[B]]", id(target_obj))
    print("[[C]] title id before rename: [", id(target_obj.title), ']')
    target_obj.title = new_title
    print("[[D]]", id(target_obj))
    print("[[E]] title id after rename: [", id(target_obj.title), "]")
    print("target_obj is obj ->", target_obj is obj)


change_object_title(obj, "My New Title")
print("[[F]] obj.title:", obj.title, '[', id(obj.title), ']')
print("[[G]] id of obj", id(obj))


class Test2:

    def __init__(self, title):
        self.title = [title]

    def add_title(self, title):
        self.title.append(title)
        # self.title += [title]
        # self.title = self.title + [title]  # make new id


obj2 = Test2('Title of Test2')
print("-01-", obj2.title)
print('-02- id of obj2.title', id(obj2.title))

obj2.add_title("Title 2")
print('-03-', obj2.title)
print('-04- id of obj2.title', id(obj2.title))
