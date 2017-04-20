from pymongo import MongoClient
import json

client=MongoClient('localhost',27017)
db=client['newdb']
collection=db.movie
mydoc=collection.find_one({},{'_id':0})
print(mydoc)
print(type(mydoc))
json.dumps(mydoc)

