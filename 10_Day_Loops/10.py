totEven = 0
totOdds = 0
for n in range(101):
    if n % 2 == 0:
        totEven += n
    else:
        totOdds += n

print(f'The sum of all evens is {totEven} and the sum of odds is {totOdds}')    
