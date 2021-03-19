import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


url = 'https://archive.ics.uci.edu/ml/datasets.php'

r = requests.get(url)
content = r.content # pegar todo conteudo dessa pagina
soup = BeautifulSoup(content, 'lxml') # modificar a leitura para que possamos trabalhar
table = soup.find(name='table', border="1", cellpadding="5") # procura a table onde vamos extrair os dados
df_full = pd.read_html(str(table))[0] # executa o dataF que gera uma colunaXlinhas
df_full.columns = ['Name', 'Data Types', 'Default Task', 'Attribute Types', 'Instances', 'Attributes', 'Year'] # coloca nome nas colunas
df_full = df_full.drop(index=0) # exclui a linha com o nome das colunas
data_for_json = {'data': df_full.to_dict('records')} # cria um dicionario com a chave data que coloca todos os dados do pandas
with open('UCL.json', 'w', encoding='utf-8') as fp: # salva o documento em 1 json
    fp.write(json.dumps(data_for_json, ensure_ascii=False))
