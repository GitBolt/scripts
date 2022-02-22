"""Simple script to migrate all data from one MongoDB instance to other"""
from pymongo import MongoClient

client1 = MongoClient("mongodb://...")
client2 = MongoClient("localhost:27017")

for db in client1.list_database_names():
    for col in client1[db].list_collection_names():
        for data in client1[db][col].find({}):
            client2[db][col].insert_one(data)
            print(db, "-", col
