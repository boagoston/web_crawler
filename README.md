#Python Web Scraping with FastAPI and BeautifulSoup

Scraping [Webscraper.io]([https://www.google.com](https://webscraper.io/test-sites/e-commerce/static/computers/laptops)) and get notebook cards in search key input and return ordered list by price with ID, Title, Description, Price, Reviews, Rating, Page

> Environment setup 
```
> python -m venv venv
> venv\Scripts\activate
> python -m pip install --upgrade pip
> pip install -r requirements.txt
> python main.py
```
> API Endpoints

Get all notebook cards
http://127.0.0.1:8000/search

get *search_key* input like lenovo

http://127.0.0.1:8000/search?search_key=lenovo

![alt text](https://github.com/boagoston/web_crawler/blob/f204a2981ce8fa2e5807b4d942c038ffb835e92e/lenovo%20api.png "api example 1")
