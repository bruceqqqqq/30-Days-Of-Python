print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(name))
print(type(nickname))
print(type(main))
print()

print('First Name:', first_name, 'Lenght:', len(first_name))
print('Last Name:', last_name, 'Lenght:', len(last_name))
print(f'Diff = {abs(len(first_name) - len(last_name))}')
print()

num_one, num_two = 5, 4

variable_total = num_one + num_two
variable_diff = num_one - num_two
variable_product = num_one * num_two
variable_division = num_one / num_two
variable_remainder = num_two % num_one
variable_exp = num_one ** num_two
variable_floor_division = num_one // num_two


print(f'A = {num_one} & B = {num_two}')
print('Variable Total:', variable_total)
print('Difference of Variables: ', variable_diff)
print('Variable Product: ', variable_product)
print('Variable Division: ', variable_division)
print('Variable Remainder: ', variable_remainder)
print('Variable Exp: ', variable_exp)
print('Variable Floor Division: ', variable_floor_division)
print()

radius = 30
pi = 3.14

area_of_circle = pi * (radius ** 2)
print('Area of Circle', area_of_circle)

print()
circum_of_circle = 2 * (pi * radius)
print('Circum of Circle', circum_of_circle)

print()
radiusInput = int(input('Radius of Circle: '))
area_of_circleInput = pi * (radiusInput**2)
print('Area of Radius Input: ', area_of_circleInput)

print()
firstname = str(input('First Name: '))
lastname = str(input('Last Name: '))
country2 = str(input('Country: '))
age2 = int(input('Age: '))
print(f'Name: {firstname}\nLast name: {lastname}\nCountry: {country2}\nAge: {age2}')

print(help('keywords'))
