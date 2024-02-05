# a = input("Enter a number: ")
# a = int(a)

def check(n):
    return not bool(n % 5)


def check3(n):
    r = n % 5
    if r == 0:
        return True
    return False


def check2(n):
    r = n % 5
    if r == 0:
        return True
    else:
        return False


def check_number(num):
    result = '{} is not integer. Bad input.'
    if isinstance(num, int):
        if num >= 10:
            if num >= 20:
                if num >= 30:
                    result = '{} >= 30'
                else:
                    result = "20 < {} < 30"
            else:
                result = "10 < {} < 20"
        else:
            result = '{} < 10'
    return result.format(num)


print(check(10), check2(10), check3(10))  # True
print(check(11), check2(11), check3(11))  # False
print(check(5), check2(5), check3(5))  # True
print(check(25), check2(25), check3(25))  # True
