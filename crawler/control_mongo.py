import pymongo as pm

FILE = open("db_config", 'r')
DB_PATH = 

class to_mongo:
    def __init__(self):
        self.mg = pm.MongoClient(DB_PATH)
        #self.mg_db = self.mg["DataPortal"]
        
    def insert_data(self, data, dest):
        self.mg_collection = self.mg_db[dest]
        try:
            self.mg_collection.insert_one(data)
        except Exception as e:
            print(e)
