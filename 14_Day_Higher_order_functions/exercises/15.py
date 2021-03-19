string = [1, 2, 'ASD', 4, (1, 2, 3), '1', 'PY']

def get_string_list(lst):
    if type(lst) == str:
        return True
    else:
        return False

only_string = filter(get_string_list, string)
print(list(only_string))
