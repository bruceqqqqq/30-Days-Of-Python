import re

with open('email_exchanges.txt') as file:
    f = file.read()
    print(f)
    regex_pattern = r"[a-z0-9]+[\._]*[a-z0-9]+[@]+\w*[.]\w*[.]?\w*"
    matches = re.findall(regex_pattern, f)
    print(matches)