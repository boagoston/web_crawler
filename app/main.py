from fastapi import FastAPI
#from .scrapper import pages, feeds

app = FastAPI()

@app.get('/pages')
def home_pages(page:str|None ='world'):
    #data = pages(page)
    #return data
    return {}

@app.get('/products')
def home_pages(page:str|None ='world'):
    #data = pages(page)
    #return data
    return {}

@app.get('/search')
def search(page:str|None ='world' ):
    return {}