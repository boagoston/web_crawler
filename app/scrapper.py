from bs4 import BeautifulSoup as Soup
import requests
from typing import Any
import sys

URL = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'

def pages(page:str)-> dict[Any]:
    request = requests.get(f'{URL}/{page}')
    html = Soup(request.content, 'html.parser')
    #card_thumbnail = html.find_all(name:'card thumbnail' , attrs:{''})
    card_thumbnail = html.find_all("div", attrs= {"class": "card thumbnail"})
    with open('div.html', 'w') as sys.stdout:
        print(card_thumbnail)
    


    
    return {} 

