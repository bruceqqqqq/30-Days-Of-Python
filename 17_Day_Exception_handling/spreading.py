list_one = [1, 2, 3]
list_two = [4, 5, 6,7]
lst = [0, *list_one, *list_two]
print(lst)

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)
