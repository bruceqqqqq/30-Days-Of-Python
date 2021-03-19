import numpy as np
import pandas as pd

# Creating data frame by a list of lists
data = [
        ['Diego', 'São Paulo', 'Guarulhos'],
        ['Amanda', 'São Paulo', 'Guarulhos'],
        ['Amandinha', 'São Paulo', 'Guarulhos']
        ]
df = pd.DataFrame(data, columns=['Names', 'State', 'City'], index=[1, 2, 3])

# Creating data frame by a dictionary

data = {
        'Name': ['Diego', 'Amanda', 'Amandinha'],
        'State': ['São Paulo','São Paulo','São Paulo'],
        'City': ['Guarulhos','Guarulhos','Guarulhos']
        }

df = pd.DataFrame(data)


# Creating a data frame from a list of dictionaries

data = [
    {'Name': 'Diego', 'State': 'São Paulo', 'City': 'Guarulhos'},
    {'Name': 'Amanda', 'State': 'São Paulo', 'City': 'Guarulhos'},
    {'Name': 'Amandinha', 'State': 'São Paulo', 'City': 'Guarulhos'}
]

df = pd.DataFrame(data)
print(df)