import pymongo as pm
from os.path import dirname, join


# 20.08.19 스타벅스에서 작업시 MongoDB Atlas 접근 제한 -> DNS 변경 후 작업 진행 

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
