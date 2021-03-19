month = str(input('Input month what you want to see what season is: ')).strip().capitalize()  # Bad English =/
seasons = {
    'Autumn': ('September', 'October', 'November'),
    'Winter': ('December', 'January', 'February'),
    'Spring': ('March', 'April', 'May'),
    'Summer': ('June', 'July', 'August')
}

if month in seasons['Autumn']:
    print(f'{month} is a month of season Autumn')
elif month in seasons['Winter']:
    print(f'{month} is a month of season Winter')
elif month in seasons['Spring']:
    print(f'{month} is a month of season Spring')
elif month in seasons['Summer']:
    print(f'{month} is a month of season Summer')
else:
    print('Month data invalid.')
