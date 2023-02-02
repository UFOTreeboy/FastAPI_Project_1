from pymongo import MongoClient

client = MongoClient("")#輸入連結語法

db = client.todo_appliaction

collection_name = db["todos_app"]