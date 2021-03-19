import re

regex_pattern = r'apple'
txt = 'Apple and Banana are fruits, And old cliche says and apple a day a doctor was been replaced by a banana'
matches = re.findall(regex_pattern, txt)
print(matches) # not show Apple
matches = re.findall(regex_pattern, txt, re.I)
print(matches) # show Apple because re.I ignore lower or upper
# or
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)
