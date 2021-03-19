import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/diego-fregolente-b75216198/',
    'https://twitter.com/bruceqq_'
]

for url in url_lists:
    webbrowser.open_new_tab(url)
