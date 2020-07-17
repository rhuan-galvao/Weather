import requests
from bs4 import BeautifulSoup as bs

page = requests.get('https://www.cptec.inpe.br/previsao-tempo/pe/recife')
soup = bs(page.content, 'html.parser')

# Relatório
relatorio = soup.find('div', class_='d-flex justify-content-center')
relatorio = relatorio.get_text()

print(relatorio)

# Temperatura Mínima
temperatura_minima = soup.find('span', class_='text-primary font-weight-bold')
temperatura_minima = temperatura_minima.get_text().strip()

print(f'Temperatura Mínima: {temperatura_minima}')

# Temperatura Máxima
temperatura_maxima = soup.find('span', class_='text-danger font-weight-bold')
temperatura_maxima = temperatura_maxima.get_text().strip()

print(f'Temperatura Máxima: {temperatura_maxima}')
