fruits = ['Banana', 'Apple', 'Grape']
vegetables = ['Alface', 'Spinafre']
fruits_and_vegetables = list()
for f, v in zip(fruits, vegetables):
    fruits_and_vegetables.append({'fruits': f, 'vegetables': v})

print(fruits_and_vegetables)

# zip can use 2 or more list to create other things