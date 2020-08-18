import pymongo as pm

class to_mongo:
    def __init__(self):
        self.mg = pm.MongoClient("localhost", 27017)
        self.mg_db = self.mg["data_portal"]
        
    def insert_data(self, data, dest):
        self.mg_collection = self.mg_db[dest]
        try:
            self.mg_collection.insert_one(data)
        except Exception as e:
            print(e)
