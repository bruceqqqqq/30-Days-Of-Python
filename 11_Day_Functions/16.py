def even_and_odds(n):
    totE = 0
    totO = 0
    for i in range(n+1):
        if i % 2 == 0:
            totE += 1
        else:
            totO += 1
    return print(f'The number of odds are {totO}\nThe number of even are {totE}')

even_and_odds(100)