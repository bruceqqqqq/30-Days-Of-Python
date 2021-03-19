from bs4 import BeautifulSoup
import requests

req = requests.get('https://archive.ics.uci.edu/ml/datasets/Adult')

if req.status_code == 200:
    print('Conexão bem sucedida.')
    content = req.content

# superior part
soup = BeautifulSoup(content, 'lxml')
tags = soup.find_all('table', border='1', cellpadding='6')
small_heading = soup.find_all('p', class_ = 'small-heading')
normal = soup.find_all('p', class_ = 'normal')
print(soup.find('span', class_ = 'heading').text)
print(soup.find('p', class_ = 'normal').text)
for t in tags:
    t = t.get_text().replace('\r', ' ')
    print(t)
for s, w in zip(small_heading, normal[19:]):
    s = s.get_text(). replace('\r', ' ')
    w = w.get_text(). replace('\r', ' ')
    print(s)
    print(w)
    print()
