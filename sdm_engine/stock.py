from datetime import date
from fastapi import HTTPException
from sdm_engine import calendar, mongo
from sdm_engine.constants import Exchange
from sdm_engine.utils import time_utils

FIELD_DAY = "day"
FIELD_EXCHANGE = "exchange"
FIELD_INSTRUMENT = "instrument"
FIELD_KEY = "key"
FIELD_VALUE = "value"
FIELD_META = "meta"


def set_stock_data(
    exchange: Exchange, instrument: str, day: date, key: str, value, meta
):
    """
    Update stock data for a particular day
    """
    # first check exchange working state
    # if the exchange not on work that day, or the record of that day not exist
    # You must correct the exchange calendar first
    # sdm safeguards overall data integrity through a strong checksum mechanism
    exchange_working_state = calendar.get_calendar_working_state(day, exchange)
    if not exchange_working_state:
        raise HTTPException(
            status_code=403,
            detail=f"exchange not on work at {day}, please check your exchange calendar",
        )
    mongo.collection_calendar.update_one(
        {
            FIELD_DAY: time_utils.date_to_datetime(day),
            FIELD_EXCHANGE: exchange,
            FIELD_INSTRUMENT: instrument,
            FIELD_KEY: key,
        },
        {"$set": {FIELD_VALUE: value, FIELD_META: meta}},
        upsert=True,
    )
