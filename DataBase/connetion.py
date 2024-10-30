import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://debrajdasgayatri:gf3OqHbhbhUDgkOH@cluster0.zes2b0w.mongodb.net")


print(client.list_database_names())

# new database
db = client['test']
col1 = db['test1']

# Inserting data
data = {"name": "Debraj", "age": 21}
col1.insert_one(data)


print(db.list_collection_names())
