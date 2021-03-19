list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

list_ = [l for l in list_of_lists for l in l for l in l]
print(list_)
