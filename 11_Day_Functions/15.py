def sumoeven(n: int):
    tot = 0
    for i in range(n+1):
        if i % 2 == 0:
            tot += 1
    return tot

print(sumoeven(100))