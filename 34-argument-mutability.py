# -- Argument Mutability --

friends_list = {
    'Mori': 10,
    'Ali': 11,
    'Alish': 12
}

print("0]", friends_list)
print("1]", id(friends_list))


def see_friend(friends, name):
    print("2]", id(friends))
    friends[name] = 0


print("2-1]", id(friends_list['Mori']))
see_friend(friends_list, 'Mori')
print("3]", friends_list)
print("3-1]", id(friends_list['Mori']))

num = 10
print("4]", num, id(num))


def change_num(n):
    n = 20
    print("4]", id(n))


print("5]", num, id(num))

print("6]", friends_list['Mori'])

num = 22


def check_id(n):
    # is check ids
    print("7]", n is num, id(n), id(num))
    n = 10


check_id(num)
print("08]", num)

age = 20
print("09]", id(age))


def increase_age(current_age):
    print("10]", id(current_age))
    current_age = current_age + 1
    print("10-1]", id(current_age))


increase_age(age)
print("11]", id(age))
print("12] age:", age)

name = 'Mori'
print("13]", id(name), name)


def change_name(new_name):
    global name
    print("14]", id(name))
    name = new_name
    print("15]", id(name))


change_name("Ali")

print("16]", id(name), name)

primes = [1, 2, 3]
print("17]", id(primes))

primes += [4, 5]
print("17]", id(primes))

primes = primes + [6, 7]
print("18]", id(primes))

primes = [1, 2, 3] + [4, 5, 6]
print("19]", id(primes))

a_list = [1, 2, 3]


def add_new_num(my_list):
    my_list += [4, 5, 6]


add_new_num(a_list)
print(a_list)
