import re

paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities, to develop an application what else can you love.'''
regex_pattern = r'[a-zA-Z]+'
matches = re.findall(regex_pattern, paragraph)
wordsinparagraph = set(matches)
mostcommun = []
for w in wordsinparagraph:
    mostcommun.append((matches.count(w), w))
mostcommunsort = list(reversed(sorted(mostcommun)))
print(mostcommunsort)
