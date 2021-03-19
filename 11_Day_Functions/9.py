def reverse_list(lst: list):
    lst.sort(reverse=True)
    for i in lst:
        print(i)


reverse_list([1, 2, 3, 4, 5])