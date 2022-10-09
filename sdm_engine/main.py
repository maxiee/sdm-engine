import uvicorn
from datetime import date
from fastapi import FastAPI, Form
from sdm_engine import calendar
from sdm_engine.constants import Exchange
from sdm_engine.mongo import init_mongo
from typing import Union, Dict

init_mongo()
app = FastAPI()


@app.get("/")
def hello():
    return "Hello, Stock Data Manager!"


def ret_map(result):
    return {"result": result}


# Calendar related APIs
@app.get("/calendar/{exchange}/{day}")
def get_calendar_working_state(day: date, exchange: Exchange):
    return ret_map(calendar.get_calendar_working_state(day, exchange))


@app.post("/calendar/{exchange}/{day}")
def set_calendar_working_state(day: date, exchange: Exchange, working: bool = Form()):
    calendar.set_calendar_working_state(day, exchange, working)


# Stock related APIs
@app.post("/stock/{exchange}/{instrument}/{day}")
def set_stock_data(
    exchange: Exchange,
    instrument: str,
    day: date,
    key: str = Form(),
    value=Form(),
    meta: Union[Dict, None]=Form(),
):
    pass


def start():
    uvicorn.run("sdm_engine.main:app", host="127.0.0.1", port=8080, reload=True)
