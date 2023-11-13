from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def index():
    return 'heyy'

@app.get('/index')
def index():
    return {'data':{'name':'shahed'}}