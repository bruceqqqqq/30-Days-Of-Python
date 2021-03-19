import json

def most_spoken_languages(filename, countries):
    languages = {}
    with open(filename, encoding='UTF-8') as file:
        r = json.load(file)
        for i in r:
            for language in i['languages']:
                if language not in languages:
                    languages[language] = 1
                elif language in languages:
                    languages[language] += 1
        sorted_languages = {k: v for k, v in reversed(sorted(languages.items(), key=lambda item: item[1]))}
        most_spoken = []
        for k, v in sorted_languages.items():
            most_spoken.append((v, k))
        return most_spoken[:countries]

print(most_spoken_languages('countries_data.json', 10))
print(most_spoken_languages('countries_data.json', 3))
