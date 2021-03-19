def decorator_with_parameters(function):
    def wrapper(a, b, c):
        function(a, b, c)
        print(f'I live in {c}.')
    return wrapper

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f'I am {first_name} {last_name}. I love to code.')

print_full_name('Diego', 'Fregolente', 'Brazil')