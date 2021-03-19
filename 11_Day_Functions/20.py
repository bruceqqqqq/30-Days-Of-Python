def prime(n):
    cont = 0
    for c in range(1, n+1):
        if n % c == 0:
            cont += 1
    if cont == 2:
        return f'{n} is prime'
    else:
        return f'{n} not prime'

print(prime(6))
