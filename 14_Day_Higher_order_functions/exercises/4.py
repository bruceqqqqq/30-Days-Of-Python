countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def print_all_countries(function):
    def wrapper(lst):
        function(lst)
        for c in lst:
            print(c, end=' ')
    return wrapper

@print_all_countries
def show_all_countries(lst):
    pass

show_all_countries(countries)