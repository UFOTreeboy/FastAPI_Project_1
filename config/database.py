from pymongo import MongoClient

client = MongoClient("")

db = client.todo_appliaction

collection_name = db["todos_app"]