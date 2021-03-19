import re

txt = '''I will become a nice developer
and give so much Proud to my grandmother and proud to my womam'''

matchfromSearch = re.search('proud', txt, re.I)
print(matchfromSearch)

span = matchfromSearch.span()
print(span)

start, end = span
substring = txt[start:end]
print(substring)

matchesfromfindall = re.findall('proud', txt, re.I)
print(matchesfromfindall)

matchesfromfindall = re.findall('[pP]roud', txt)
print(matchesfromfindall)

matchesfromfindall = re.findall('proud|Proud', txt) # | is used in python
print(matchesfromfindall)

sub = re.sub('proud|Proud', 'love', txt)
print(sub)
