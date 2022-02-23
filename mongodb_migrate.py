"""Simple script to migrate all data from one MongoDB instance to other"""
from pymongo import MongoClient

root_client: MongoClient = MongoClient("mongodb://...")
new_client: MongoClient = MongoClient("localhost:27017")


def db_to_db() -> None:
    for db in root_client.list_database_names():
        for col in root_client[db].list_collection_names():
            for data in root_client[db][col].find({}):
                try:
                    new_client[db][col].insert_one(data)
                    print(db, "-", col)
                except Exception as e:
                    print(db, "-", col, "\n", e)
                    

def db_to_local() -> None:
    for db in root_client.list_database_names():
        for col in root_client[db].list_collection_names():
            for doc in root_client[db][col].find({}):
                try:
                    os.makedirs(f"backup/{db}/{col}/")
                except:
                    continue
                with open(f"backup/{db}/{col}/{doc['_id']}", "w") as f:
                    f.write(str(json.dumps(doc)))
                    print(db, " - ", doc)

                
