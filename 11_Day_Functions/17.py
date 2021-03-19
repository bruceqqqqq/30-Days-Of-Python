def factorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

print(factorial(5))