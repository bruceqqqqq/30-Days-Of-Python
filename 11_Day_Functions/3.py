def add_all_nums(*nums):
    tot = 0
    for n in nums:
        if isinstance(n, int): # or use type(n) to verify
            tot += n
        else:
            print(f'{n} is not a number')
    return tot

print(add_all_nums(2, 'b', 3))
