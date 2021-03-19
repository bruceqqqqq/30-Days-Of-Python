brothers = ('Draven', 'Lee Sin', 'Pablo')
sisters = ('Kaisa', 'Vayne', 'Miss Fortune')
siblings = brothers + sisters
family = ('Vivian', 'Julio') + siblings
mother, father, *siblings = family
brothers = tuple(siblings[:3])
sisters = tuple(siblings[3:])
print('Mother:', mother, 'Father:', father, 'Brothers:', brothers, 'Sisters:', sisters)
