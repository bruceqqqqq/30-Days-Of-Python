def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper

def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator # chama os decoradores de baixo pra cima, p isso upper primeiro dps split pq upper n funfa list
def welcome():
    return 'Hello Friend, to night we will destroy the city.'

print(welcome())

