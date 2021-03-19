it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f'Biggest companies of IT in the market{it_companies}')
print(f'Total of companies {len(it_companies)}')
print(f'First company {it_companies[0]}, Middle {it_companies[len(it_companies)//2]}, Last {it_companies[-1]}')
it_companies[6] = 'Youtube'
print(f'New list of companies {it_companies}')
it_companies.append('Amazon')
it_companies.insert(4, 'Totvs')
it_companies[0] = it_companies[0].upper()
it_companies = '#'.join(it_companies)
print(it_companies)
if 'IBM' in it_companies:
    print('IBM already in the list')
it_companies = it_companies.split('#')
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
it_companies = it_companies[3:]
print(it_companies)
it_companies = it_companies[:-3]
print(it_companies)
it_companies.pop(len(it_companies) // 2)
print(it_companies)
del it_companies[-1]
print(it_companies)
del it_companies[0]
print(it_companies)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies[:3])
print(it_companies[-3:])
print(it_companies[len(it_companies)//2])
del it_companies
try:
    print(it_companies)
except:
    print('End of List')
