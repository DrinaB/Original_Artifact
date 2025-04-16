from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter (object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient(f'mongodb://{username}:{password}@nv-desktop-services.apporto.com:32759/AAC?authSource=aac')
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD
    #  C in CRUD
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  
            if insert.acknowledged:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Complete this create method to implement the R in CRUD
    def read(self, readData):
        if readData:
            data = list(self.database.animals.find(readData, {"_id": False}))
            
        else:
            data = list(self.database.animals.find({}, {"_id": False}))
        return data
    
 # U in CRUD
    def update(self, query, new_values):
        if query and new_values:
            update_result = self.database.animals.update_many(query, {"$set": new_values})
            return update_result.modified_count
        else:
            raise Exception("Query and new values cannot be empty")
        
 # D in CRUD
    
    def delete(self, query):
        if query:
            delete_result = self.database.animals.delete_many(query)
            return delete_result.deleted_count
        else:
            raise Exception("Query cannot be empty")