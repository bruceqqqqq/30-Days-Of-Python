def convert_celsius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return str(fahrenheit) + ' F°'


celsius = convert_celsius_to_fahrenheit(int(input('Press Celsius to Fahrenheit: ')))
print(celsius)