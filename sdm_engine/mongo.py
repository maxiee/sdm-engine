from pymongo import MongoClient

client = None

def init_mongo():
    global client
    client = MongoClient()