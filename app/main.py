from fastapi import FastAPI
from .scrapper import search

app = FastAPI()

@app.get('/search')
def search_product(search_key:str|None = None):
    if(search_key):
        search_key = str.lower(search_key)
    data = search(search_key)
    return data
    
