import requests

url = 'http://www.gutenberg.org/files/1112/1112.txt' # recebe url
link = requests.get(url) # carrega url
text = link.text # carrega texto recebido pelo get
words = [words for words in text.split(' ') for w in words.strip()] # cria uma lista separando palavras por espaços e removendo os espaços
word_counter = {} # dicionario onde vamos adicionar as palavras e quantidades
for word in words: # pra cada palavra em palavras, adiciona uma chave "palavra" e 1 ou +1
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
result = {k:v for k, v in reversed(sorted(word_counter.items(), key=lambda item: item[1]))} # sort reverse by value
most_frequents_words = [(k, v) for k, v in result.items()] # return to a list
print(most_frequents_words[:10])
