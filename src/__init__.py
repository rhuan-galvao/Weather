from bs4 import BeautifulSoup
from requests import get


class scrap:
    def __init__(self, state, city):
        self.html = get(f"https://www.cptec.inpe.br/previsao-tempo/{state}/{city}").content
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def max(self):
        temp = self.soup.find("span", class_="text-danger font-weight-bold")

        return temp.get_text().strip()

    def min(self):
        temp = self.soup.find("span", class_="text-primary font-weight-bold")

        return temp.get_text().strip()

    def relatorio(self):
        relatorio = self.soup.find('div', class_='d-flex justify-content-center')
        
        return relatorio.get_text().strip()