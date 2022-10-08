from datetime import date
from sdm_engine import mongo

def set_calendar_day(day: date, working: bool):
    return mongo.collection_calendar.update_one(
        {
            'date': day
        },
        {
            '$set': {
                "working": working
            }
        },
        upsert=True)