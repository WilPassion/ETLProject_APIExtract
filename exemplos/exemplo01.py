# BIBLIOTECA
import requests

# REQUEST PAGINA 
url = 'https://www.youtube.com/'
resposta = requests.get(url)
print(resposta)