import pandas as pd
import numpy as np


data = [
    {'Name':'Diego', 'Country':'Brazil', 'State':'São Paulo'},
    {'Name':'Amanda', 'Country':'Brazil', 'State':'São Paulo'},
    {'Name':'Amandinha', 'Country':'Brazil', 'State':'São Paulo'}
]

df = pd.DataFrame(data)

# Add a Column to a data frame
weights = [125, 65, 11]
df['Weight'] = weights
heights = np.array([182, 162, 11])
df['Height'] = heights * 0.01 # convert int altura para float ficando 1metros82cm

def calc_imc():
    weights = df['Weight']
    heights = df['Height']
    imc = []
    for w, h in zip(weights,heights):
        i = w / (h*h)
        imc.append(i)
    return imc

imc = calc_imc()
df['IMC'] = imc
df['IMC'] = round(df['IMC'], 1) # change to a float with 1 point

birth_year = [1996, 1991, 2020]
current_year = pd.Series(2021, index=[0, 1, 2]) # adiciona 2021 em todos os campos 0 1 2
df['Birth Year'] = birth_year
df['Current Year'] = current_year

df['Birth Year'] = df['Birth Year'].astype('int') # change to int32
# print(df['Birth Year'].dtype)
df['Current Year'] = df['Current Year'].astype('int') # change to int32
# print(df['Current Year'].dtype)

ages = df['Current Year'] - df['Birth Year']
df['Age'] = ages

# print(df[df['Age'] > 22]) # Diego Amanda
print(df[df['Age'] < 22]) # Amandinha