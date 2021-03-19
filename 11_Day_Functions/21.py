def unique_itens(lst: list):
    c = 0
    for i in lst:
        if lst.count(i) == 1:
            c += 1
    if len(lst) == c:
        print('All itens in list are unique')
    else:
        print('Not unique itens')

unique_itens(['a', 'a', 'b', 'c'])
unique_itens([1, 2, 3])
