countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten = [p.upper() for p in countries for p in p for p in p]
print(flatten)