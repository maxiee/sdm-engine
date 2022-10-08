from pymongo import MongoClient

client = None

def init_mongo():
    client = MongoClient()