from datetime import date
from fastapi import HTTPException

from sdm_engine import mongo
from sdm_engine.constants import Exchange
from sdm_engine.utils import time_utils

FIELD_DAY = "day"
FIELD_EXCHANGE = "exchange"
FIELD_WORKING = "working"


def get_calendar_working_state(day: date, exchange: Exchange):
    """
    Get the working date of the stock exchange
    """
    ret = mongo.collection_calendar.find_one(
        {FIELD_DAY: time_utils.date_to_datetime(day), FIELD_EXCHANGE: exchange}
    )
    if ret:
        return ret[FIELD_WORKING]
    raise HTTPException(status_code=404, detail="record not found")


def set_calendar_working_state(day: date, exchange: Exchange, working: bool):
    """
    Set the working date of the stock exchange
    """
    mongo.collection_calendar.update_one(
        {FIELD_DAY: time_utils.date_to_datetime(day), FIELD_EXCHANGE: exchange},
        {"$set": {FIELD_WORKING: working}},
        upsert=True,
    )
