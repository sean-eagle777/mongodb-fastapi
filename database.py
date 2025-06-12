from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://seanhsieh2014:5180551805Sean@cluster0.xfv28db.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


client = AsyncIOMotorClient(MONGO_URL)
database = client.get_database("<database_name>")
collection = database.get_collection("<collection_name>")
