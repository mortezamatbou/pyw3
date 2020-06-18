a_set = ['a', 'b', 'a', 'b', 'c', 'd', 'c', 'd', 'e', 'f']


def remove_duplicates(list_duplicates):
    if type(list_duplicates) == set:
        return None
    new_list = []
    for x in list_duplicates:
        if x not in new_list:
            new_list.append(x)

    return new_list


removed = remove_duplicates(a_set)

print(removed)
