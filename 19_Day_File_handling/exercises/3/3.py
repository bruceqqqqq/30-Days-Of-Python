import json

def most_populated_countries(filename, countries):
    with open(filename, encoding='UTF-8') as file:
        f = json.load(file)
        countries_population = []
        for p in f:
            countries_population.append({'country': p['name'], 'population': p['population']})
        most_populated_countries_result = list(reversed(sorted(countries_population, key=lambda k: k['population'])))
        return most_populated_countries_result[:countries]

print(most_populated_countries('countries_data.json', 3))
