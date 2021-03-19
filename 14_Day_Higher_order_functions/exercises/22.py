from countries import countries

name_sort = sorted(countries, key=lambda k: k['name'])

population_sort = list(reversed(sorted(countries, key=lambda  k: k['population'])))

most_spoken_languages = {}
for l in countries:
    for l in l['languages']:
        if l not in most_spoken_languages:
            most_spoken_languages[l] = 1
        elif l in most_spoken_languages:
            most_spoken_languages[l] += 1

# most_spoken_languages_new = {k: v for k, v in list(reversed(sorted(most_spoken_languages.items(), key=lambda item: item[1])))}
# most_spoken_languages_new = [languages for languages in most_spoken_languages_new.keys()]
# top10 = most_spoken_languages_new[:10]
# print(top10)