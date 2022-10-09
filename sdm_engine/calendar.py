from datetime import date

from sdm_engine import mongo
from sdm_engine.constants import Exchange
from sdm_engine.utils import time_utils


def set_calendar_day(day: date, exchange: Exchange, working: bool):
    """
    Set the working date of the stock exchange
    """
    mongo.collection_calendar.update_one(
        {"day": time_utils.date_to_datetime(day), "exchange": exchange},
        {"$set": {"working": working}},
        upsert=True,
    )
