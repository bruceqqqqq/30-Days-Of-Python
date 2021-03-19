from random import randint

def random_numbers():
    array = list()
    while len(array) != 7:
        n = randint(0, 9)
        if n not in array:
            array.append(n)
    return array

print(random_numbers())
