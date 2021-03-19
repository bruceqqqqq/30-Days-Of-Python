def generate_full_name():
    first_name = 'Diego'
    last_name = 'Fregolente Biagi'
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())

def add_two_numbers():
    a = int(input('First number: '))
    b = int(input('Second number: '))
    total = a + b
    return total

print('Total: ', add_two_numbers())

def greetings(name: str):
    message = name + ', Welcome to the Python for Everyone!'
    return message

print(greetings('Diego'))

def add_ten(number: int):
    ten = 10
    return number + ten

print(add_ten(90))

def square_number(x: int):
    return x * x

print(square_number(2))

def area_of_circle(radius: int):
    pi = 3.14
    area = pi * (radius ** 2)
    return area

print('Area of circle:', area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for n in range(n+1):
        total += n
    return total

print(sum_of_numbers(10))
print(sum_of_numbers(100))

def full_name(first, second, thirty):
    space = ' '
    full = first + space + second + space + thirty
    return full

print(full_name('Diego', 'Fregolente', 'Biagi'))

def sum_two_numbers(a: int, b: int):
    return a + b

print(sum_two_numbers(4, 5))

def calculate_age(birthday_year, actual_year):
    return actual_year - birthday_year

print('Your age:', calculate_age(1996, 2021))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # first calculate mass * gravity, after change to str, and conca with ' N'
    return weight # return string generate above
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

def print_full_name(firstname, lastname) -> object:
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break
    return False
print(is_even(10)) # True
print(is_even(7)) # False

def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num
    return total
print(sum_all_nums(2, 3, 5))

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')