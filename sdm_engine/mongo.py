from pymongo import MongoClient

client = None
database = None
collection_calendar = None

def init_mongo():
    print('init_mongo')
    global client
    global database
    global collection_calendar

    client = MongoClient()
    database = client['sdm']
    collection_calendar = database['calendar']