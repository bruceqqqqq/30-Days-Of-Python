import requests
import math

url = 'https://restcountries.eu/rest/v2/all'

link = requests.get(url)

countries = link.json()

dict_of_countries = []

for d in countries:
    if d['area'] != None:
        dict_of_countries.append({'name': d['name'], 'area': int(d['area'])})

sort_dict_by_value = list(reversed(sorted(dict_of_countries, key=lambda k: k['area'])))

top10 = sort_dict_by_value[:10]

print(top10)