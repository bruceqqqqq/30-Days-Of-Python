import requests # not from flask/request

# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
#
# response = requests.get(url)
#
# print(response)
# print(response.status_code)
# print(response.headers)
# letters = response.text
# print(type(letters))

url = 'https://restcountries.eu/rest/v2/all'

response = requests.get(url)

print(response)
print(response.status_code)
countries = response.json()
print(countries[1])