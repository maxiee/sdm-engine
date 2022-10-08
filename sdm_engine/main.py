import uvicorn
from datetime import date
from fastapi import FastAPI, HTTPException, Form
from sdm_engine import calendar
from sdm_engine.mongo import init_mongo

app = FastAPI()

@app.get('/')
def hello():
    return "Hello, Stock Data Manager!"

# Calendar related APIs
@app.get('/calendar/{day}')
def get_calendar_day(day: date) -> bool:
    raise HTTPException(
        status_code=404, 
        detail="record not found")

@app.post('/calendar/{day}')
def set_calendar_day(day: date, working: bool = Form()):
    calendar.set_calendar_day(day, working)

def start():
    init_mongo()
    uvicorn.run(
        'sdm_engine.main:app', 
        host='127.0.0.1',
        port=8080,
        reload=True)