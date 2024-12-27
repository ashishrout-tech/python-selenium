from pymongo import MongoClient
from datetime import datetime

class DatabaseService:
    def __init__(self, mongo_uri):
        self.client = MongoClient(mongo_uri)
        self.db = self.client["selenium"]
        self.collection = self.db["trends"]
    
    def insert_data(self, data):
        try:
            result = self.collection.insert_one(data)
            return result.inserted_id
        except Exception as e:
            print(f"Error inserting data: {e}")
            return None
    
    def get_record_by_id(self, record_id):
        return self.collection.find_one({"_id": record_id})