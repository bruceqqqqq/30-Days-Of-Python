def type_itens(lst: list):
    typeoflist = type(lst[0])
    for i in lst:
        if type(i) != typeoflist:
            return 'Not all datatype is the same in this list'
    if type(i) == typeoflist:
        return 'All data type is the same in this list'


print(type_itens([1, 2, 3]))
print(type_itens(['a', 2, 3]))
