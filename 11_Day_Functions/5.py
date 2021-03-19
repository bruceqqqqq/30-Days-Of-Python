def check_season(month: str):
    seasons = {
        'Autumn': ('September', 'October', 'November'),
        'Winter': ('December', 'January', 'February'),
        'Spring': ('March', 'April', 'May'),
        'Summer': ('June', 'July', 'August'),
    }
    if month in seasons['Autumn']:
        print(f'{month} is a month of Autumn')
    elif month in seasons['Winter']:
        print(f'{month} is a month of Winter')
    elif month in seasons['Spring']:
        print(f'{month} is a month of Spring')
    elif month in seasons['Summer']:
        print(f'{month} is a month of Summer')


check_season(str(input('Check Season of a Month: ').strip().capitalize()))