import pymongo


def ConnectToMongo():
    try:
        client = pymongo.MongoClient("mongodb+srv://test:test@eco-lisisdb.akphrcr.mongodb.net/?retryWrites=true&w=majority")
        return client
    except pymongo.errors.ConnectionError as e:
        print("Error connecting to MongoDB:", e)
        
        
if ConnectToMongo():
    print("connected")        