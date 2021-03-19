countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten = [p for p in countries for p in p]
dictofcountries = [{'country': flatten[i][0].upper(), 'city': flatten[i][1].upper()} for i in range(len(flatten))]
print(dictofcountries)
