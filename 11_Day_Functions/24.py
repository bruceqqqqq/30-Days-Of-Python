def most_spoken_languages():
    languages = ['English', 'Chinese', 'Hindi', 'Spanish', 'French',
                 'Standard Arabic', 'Bengali', 'Russian', 'Portuguese', 'Indonesian']
    print('Ranking Languages Speak: ')
    for p, i in enumerate(languages):
        print(p+1, i)

def most_world_population():
    countries = ['China', 'India', 'United States', 'Indonesian', 'Pakistan',
                 'Nigeria', 'Brazil', 'Bangladesh', 'Russia', 'Mexico']
    print('Ranking World Population: ')
    for p, i in enumerate(countries):
        print(p+1, i)

most_spoken_languages()
most_world_population()
