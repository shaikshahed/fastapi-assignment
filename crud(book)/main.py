from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

@app.get('/')
def index():
    return 'heyy'

# class Blog(BaseModel):
#     title:str
#     body:str
#     published:bool

# @app.post('/blog')
# def create(request:Blog):
#     return request
#     return {'data':'blog is created'}

# @app.get('/blog/{id}')
# def create_id(id:int):
#     return {'id':id}

data = []
class Book(BaseModel):
   id: int
   title: str
   author: str
   publisher: str

@app.post("/book")
def add_book(book: Book):
   data.append(book.dict())
   return data
# @app.get("/list")
# def get_books():
#    return data

@app.get("/book/{id}")
def get_book(id: int):
   return data[id]

@app.put("/book/{id}")
def add_book(id: int, book: Book):
   data[id-1] = book
   return data

@app.delete("/book/{id}")
def delete_book(id: int):
   data.pop(id-1)
   return data


