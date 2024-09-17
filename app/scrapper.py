from bs4 import BeautifulSoup as Soup
import requests

URL = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'

def pages(page:str)-> dict[Any]:
    requests.get(f'{URL}/{page}')
    
    return {} 
