# def welcome():
#     return 'Welcome to the Python' # basic function
#
# def uppercase_decorator(function): # parameter function
#     def wrapper(): # function inside of uppercase
#         func = function() # variable == function()
#         make_uppercase = func.upper() # transforma o retorno da função chamada em upper
#         return make_uppercase # retorno do retorno da função em CAPS
#     return wrapper # chama a função wrapper que ira retornar o acima return make_uppercase
#
#
# g = uppercase_decorator(welcome) # chama a função com outra função e returna para 'g'
# print(g())

# Example below with decorator

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper

@uppercase_decorator
def welcome():
    return 'Hello Friend.'

print(welcome())
