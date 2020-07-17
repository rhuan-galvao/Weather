from requests import get
from bs4 import BeautifulSoup as bs



def request() -> str:
    page = get(f'https://www.cptec.inpe.br/previsao-tempo/pe/recife')
    soup = bs(page.content, 'html.parser')

    return soup

def relatorio() -> None:
    relatorio = request().find('div', class_='d-flex justify-content-center')
    
    return relatorio.get_text()

def temp_minima() -> None:
    temperatura_minima = request().find('span', class_='text-primary font-weight-bold')
    
    return temperatura_minima.get_text().strip()

def temp_maxima() -> None:
    temperatura_maxima = request().find('span', class_='text-danger font-weight-bold')
    
    return temperatura_maxima.get_text().strip()

request()