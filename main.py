from fastapi import FastAPI
from typing import Union

app = FastAPI()
@app.get('/')

def read_toot():
    return{
        'hello':'world'
    }