# Normal Function
def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def absolute(n):
    if n >= 0:
        return n
    else:
        return - n # if n = negative change to - n - n = n

def higher_order_functions(str):
    if str == 'square':
        return square
    elif str == 'cube':
        return cube
    elif str == 'absolute':
        return absolute

result = higher_order_functions('square')
print(result(3))
result = higher_order_functions('cube')
print(result(3))
result = higher_order_functions('absolute')
print(result(- 3))

#Closure in Python
def add_ten():
    ten = 10

    def add(num):
        return num + ten
    return add

close_result = add_ten()
print(close_result(5))
print(close_result(10))