import pymongo as pm
from os.path import dirname, join

current_dir = dirname(__file__)
FILE = open(dirname(__file__)+"/db_config", "r", encoding="utf8")
DB_PATH = FILE.read()

class to_mongo:
    def __init__(self):
        self.mg = pm.MongoClient(DB_PATH)
        self.mg_db = self.mg["DataPortal"]
        
    def insert_data(self, data, dest):
        self.mg_collection = self.mg_db[dest]
        try:
            self.mg_collection.insert_one(data)
        except Exception as e:
            print(e)
