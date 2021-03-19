names = [[('Diego', 'Fregolente')], [('Amanda', 'Raisa')], [('Vivian', 'Fregolente')]]
test = [n for n in names for n in n]
test1 = [' '.join(test[n]) for n in range(len(test))]
print(test1)
