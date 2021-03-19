# higher order function == function who need another function or return function
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, *args):
    summation = f(*args)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

# closure == def a function inside of a function and can acess the values of this function inside
def add_ten():
    ten = 10

    def add(num):
        return num + ten
    return add

close_result = add_ten()
print(close_result(5))

# decorator == create a new func to another func, we need to a wrapper and uses a decorator before a function
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