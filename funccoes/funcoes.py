import requests

# fazendo uma requisição
r = requests.get('https://www.google.com')

# status
r.status_code

# Informações do HTML
r.headers

# Pegando informações de DATE no header
r.headers['Date']

# Pegando informações de texto
r.text

# API com python
