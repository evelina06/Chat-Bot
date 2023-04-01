import pymongo as pymongo

client = pymongo.MongoClient("mongodb+srv://bot:JXzRunBCX68Ac4MT@biology.mr7dsze.mongodb.net/?retryWrites=true&w=majority")
db = client.user.test


print(db.delete_one({'_id': 123}))
