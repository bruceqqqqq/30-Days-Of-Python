import requests

url = 'https://api.thecatapi.com/v1/breeds'
resposte = requests.get(url)
cats = resposte.json()
dict_cats = {}
for i in cats:
    dict_cats[i['id']] = {
    'name':i['name'], 'weight': i['weight']['metric'], 'Avarage': ((int(i['weight']['metric'][4]) - int(i['weight']['metric'][0])) /2 )
    }

print(dict_cats)