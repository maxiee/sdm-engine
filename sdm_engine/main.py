import uvicorn
from datetime import date
from fastapi import FastAPI

from sdm_engine.mongo import init_mongo

app = FastAPI()

@app.get('/')
def hello():
    return "Hello, Stock Data Manager!"


# Calendar related APIs
@app.get('/calendar/{day}')
def get_calendar_day(day: date):
    return day

def start():
    init_mongo()
    uvicorn.run(
        'sdm_engine.main:app', 
        host='127.0.0.1',
        port=8080,
        reload=True)