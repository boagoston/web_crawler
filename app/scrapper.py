from bs4 import BeautifulSoup as Soup
import requests
from typing import Any
import sys

URL = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'

def search(search_key:str)-> dict[Any]:
    result_cards = []
    index = 0
    request = requests.get(f'{URL}')
    html = Soup(request.content, 'html.parser')
    print(search_key)
    
    
    #Recorta o numero total de paginas
    total_page_numbers = html.find_all("ul", attrs= {"class": "pagination"})
    total_page_numbers = html.find_all("li", attrs= {"class": "page-item"})
    total_page_numbers = total_page_numbers[-2].text
    total_page_numbers= total_page_numbers

    for page in range(1, int(total_page_numbers)+1):
        
        url_with_page = f"{URL}?page={page}"
        request = requests.get(f'{url_with_page}')
        html = Soup(request.content, 'html.parser')
        
        #Recorta o numero total de paginas
        total_page_numbers = html.find_all("ul", attrs= {"class": "pagination"})
        total_page_numbers = html.find_all("li", attrs= {"class": "page-item"})
        total_page_numbers = total_page_numbers[-2].text
        total_page_numbers= total_page_numbers
        
        

        

        #Recorta todos os cards da pagina
        card_thumbnail = html.find_all("div", attrs= {"class": "card thumbnail"})      
        
        for (i, div) in enumerate(card_thumbnail):
            index+=1
            row = {'id': None, 'title': None, 'description': None, 'price': None, 'reviews': None, 'rating': None, 'page': None,}
            row['id'] = index
            row['title'] = div.find('a', class_='title').get('title')
            row['description'] = div.find('p', class_='description card-text').text.strip()
            
            if(row['description']) and (row['title']) and (search_key):
                if not(search_key in str.lower(row['title'])):
                    continue
                if not(search_key in str.lower(row['title'])):
                    continue    

            row['price'] = div.find('h4', class_='price float-end card-title pull-right').text.strip()
            row['reviews'] = div.find('p', class_='review-count float-end').text.strip()
            row['rating'] = div.find('p', attrs={'data-rating': True})
            row['rating'] = row['rating'].get('data-rating')
            row['page'] = page

            result_cards.append(row)
            
            

    
    return {'total': len(result_cards), 'result_cards': result_cards} 

