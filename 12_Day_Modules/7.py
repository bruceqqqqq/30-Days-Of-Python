from random import shuffle

def shuffle_list(lst: list):
    shuffle(lst)
    return lst


print(shuffle_list([1, 2, 3, 4, 5]))