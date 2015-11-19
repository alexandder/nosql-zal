import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.nosql

subreddits = db.subreddits.aggregate([{"$group" : {"_id" : "$lang", "count" : {"$sum" : 1}}},
                                      {"$sort" : {"count" : -1}},
                                      {"$limit" : 10}])

print(list(subreddits))
