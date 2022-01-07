from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://faraz:affa@cluster0.xwnk6.mongodb.net/ffrooms?retryWrites=true&w=majority")
db = client.ffrooms  # db selecting database
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}
mydb=db.users  #connecting to collection
# ffroom_id=ffrooms.insert_one(post).inserted_id
# print(ffroom_id)
# print(db)
