from datetime import date
from datetime import datetime


def date_to_datetime(date: date):
    return datetime.combine(date.today(), datetime.min.time())
