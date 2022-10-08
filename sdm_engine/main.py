import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return "Hello, Stock Data Manager!"

def start():
    uvicorn.run(
        'sdm_engine.main:app', 
        host='127.0.0.1',
        port=8080,
        reload=True)