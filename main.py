from pymongo import MongoClient # importing the library pymongo and accesing the attribute MongoClient
from password import cluster # im importing the connection string for the database from another file for secuirty
import datetime # importing the library to use time

cluster = cluster # variable used to define the connection string
client = MongoClient(cluster) # variable used to login using the previously mentioned connection string

print(client.list_database_names()) # print the list of names inside the database

db = client.profile # variable the defines a connection between the client and a specifc shard

user_name = input("Enter the user name of your task ") # input asking for a the name of a task
description = input("Heloo Input User Description ") # input asking for a users description of their todo list

print(db.list_collection_names()) # print list of colleciton names

todo_list =  {"name": f"{user_name}", "description": f"{description}", "status": "open" ,
              "tags": ["python", "coding"], "date": str(datetime.datetime.utcnow())}

todos = db.todos # creating a shard for the todo list inside the database

result = todos.insert_one(todo_list) # publishing the information 


