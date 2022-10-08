import uvicorn
from datetime import date
from fastapi import FastAPI, HTTPException, Form
from sdm_engine import calendar
from sdm_engine.constants import Exchange
from sdm_engine.mongo import init_mongo

init_mongo()
app = FastAPI()


@app.get("/")
def hello():
    return "Hello, Stock Data Manager!"


# Calendar related APIs
@app.get("/calendar/{exchange}/{day}")
def get_calendar_day(day: date) -> bool:
    raise HTTPException(status_code=404, detail="record not found")


@app.post("/calendar/{exchange}/{day}")
def set_calendar_day(day: date, exchange: Exchange, working: bool = Form()):
    calendar.set_calendar_day(day, exchange, working)


def start():
    uvicorn.run("sdm_engine.main:app", host="127.0.0.1", port=8080, reload=True)
