from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup as bs

def pesquisar(music):
	pagina = requests.get('https://www.youtube.com/results?search_query=' + quote_plus(music))
	soup_pagina = bs(pagina.text, 'html.parser')
	soup = soup_pagina.select('h3 a')
	titulo_link = {}
	for link in soup:
		titulo_link['song'] = link.get('href')
		break
	return titulo_link