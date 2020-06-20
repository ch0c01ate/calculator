from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://admin:Sp6LxKdfVRCxDK06@calculator-zczyd.azure.mongodb.net/calculator?retryWrites=true&w=majority"
)
db = client.calculator
expressions = db.expressions