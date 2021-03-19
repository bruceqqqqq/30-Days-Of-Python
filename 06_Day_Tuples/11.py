fruits = ('Banana', 'Apple')
vegetables = ('Asian Greens', 'Asparagus')
animal_products = ('Milk', 'Eggs')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_it = list(food_stuff_tp)
first_three = food_stuff_tp[:3]
last_item = food_stuff_it[-1]
del food_stuff_tp
print(food_stuff_tp) # error, because del.