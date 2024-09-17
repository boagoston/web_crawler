from fastapi import FastAPI
from .scrapper import pages

app = FastAPI()

@app.get('/pages')
def home_pages(page:str|None =''):
    data = pages(page)
    return data
    

@app.get('/products')
def home_pages(page:str|None ='world'):
    #data = pages(page)
    #return data
    return {}

@app.get('/search')
def search(page:str|None ='world' ):
    return {}