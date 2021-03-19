import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'lxml')
table = soup.find(name='table', class_ ='wikitable', style='text-align:center;')
df = pd.read_html(str(table))[0]
df = df.drop_duplicates(subset=['President', 'President.1'])
df = df[:-1]
my_data = df.to_dict('records')
with open('presidents.json', 'w', encoding='utf-8') as file:
     file.write(json.dumps(my_data, ensure_ascii=False))


