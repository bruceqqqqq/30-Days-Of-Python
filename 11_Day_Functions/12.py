def remove_item(lst: list, item):
    lst.remove(item)
    return lst

print(remove_item([1, 2, 3, 4], 4))
print(remove_item(['a', 'b', 'c'], 'c'))