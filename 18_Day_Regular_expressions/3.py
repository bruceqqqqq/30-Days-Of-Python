import re

def is_valid_variable(string: str) -> bool:
    return bool(re.findall('^[^\d\W]\w*\Z', string))

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # F
print(is_valid_variable('1first_name')) # F
print(is_valid_variable('firstname')) # True

