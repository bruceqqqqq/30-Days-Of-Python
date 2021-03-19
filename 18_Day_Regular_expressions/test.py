import re

# Square Bracket
txt = 'Apple and Banana and apple and banana'
regex_pattern = r'[Aa]pple|[Bb]anana'
matches = re.findall(regex_pattern, txt)
print(matches)

# Escape character(\) using RegEx
txt = 'February 11, 2021.'
regex_pattern = r'\d' # \d means digits
matches = re.findall(regex_pattern, txt)
print(matches)

# One More times (+)
regex_pattern = r'\d+'  # d+ means digits, and + mean one or more times
txt = 'This regular expression example was made on December 6,  2019.'
matches = re.findall(regex_pattern, txt)
print(matches)

# Period(.)
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches) # ['and banana are fruits']

# Zero or more times(*)
regex_pattern = r'[a].*'  # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# Zero or one time(?)

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

# Quantifier in RegEx

txt = 'This regular expression example was made on December 6,  2019.'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019']

txt = 'This regular expression example was made on December 6,  2019.'
regex_pattern = r'\d{1,4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019']

# Cart ^
txt = 'This regular expression example was made on December 6,  2019.'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

txt = 'This regular expression example was made on December 6,  2019.'
regex_pattern = r'[^A-Za-z .,]+'  # ^ in set character means negation, not A to Z, not a to z, no space, no . or ,
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019.']

