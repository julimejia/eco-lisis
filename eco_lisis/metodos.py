
import pymongo


def ConnectToMongo():
    try:
        client = pymongo.MongoClient("mongodb+srv://test:test@eco-lisisdb.akphrcr.mongodb.net/?retryWrites=true&w=majority")
        return client
    except pymongo.errors.ConnectionError as e:
        print("Error connecting to MongoDB:", e)

if ConnectToMongo():
    print("connected")        
    
    
    
def SearchDocuments(client: pymongo.MongoClient, db_name: str, collection_name: str, filter):
    try:
        # Acceder a la base de datos y la colección
        db = client[db_name]
        collection = db[collection_name]
        # Realizar la búsqueda
        results = collection.find(filter)

        return results
    
    except pymongo.errors.CollectionInvalid as e:
        print("Error triying to access to Collection:", collection_name, ":", e)