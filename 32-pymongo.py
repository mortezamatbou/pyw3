# -- Python MongoDB --
# Python needs a MongoDB driver to access the MongoDB database.
# run command in linux for install pymongo driver from pip
# cmd-> sudo pip3 install pymongo

# + Test PyMongo
# To test if the installation was successful, or if you already have "pymongo" installed, create a Python page
# with the following content:

import pymongo

# To create a database in MongoDB, start by creating a MongoClient object,
# then specify a connection URL with the correct ip address and the name of the database you want to create.
# connect to mongo
client = pymongo.MongoClient('mongodb://localhost:27017/')

# + Creating a Database
# MongoDB will create the database if it does not exist, and make a connection to it.
# ::IMPORTANT:: In MongoDB, a database is not created until it gets content!

db_name = client['my_db_name']
# MongoDB waits until you have created a collection (table), with at least one document (record) before it actually
# creates the database (and collection).

# ::REMEMBER:: In MongoDB, a database is not created until it gets content, so if this is your first time
# creating a database, you should complete the next two chapters (create collection and create document)
# before you check if the database exists!

# - Check if Database Exists

print(client.list_database_names())
if "my_db_name" in client.list_database_names():
    print("my_db_name exists.")
else:
    print("my_db_name not exists.")

# + Python MongoDB Create Collection
# A collection in MongoDB is the same as a table in SQL databases.

# + Creating a Collection
# To create a collection in MongoDB, use database object and specify the name of the collection you want to create.
# MongoDB will create the collection if it does not exist.
client = pymongo.MongoClient('mongodb://localhost:27017/')

sports_db = client['sports']
print(sports_db.list_collection_names())

# + Python MongoDB Insert Document
# A document in MongoDB is the same as a record in SQL databases.

# collection -> table in sql
# document   -> record(row) in sql

# + Insert Into Collection
# To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.
# The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s)
# of each field in the document you want to insert.

client = pymongo.MongoClient("mongodb://localhost:27017/")

sports = client['sports']
hockey = sports['hockey']

"""
database -> 'sports'
                    -> collections:
                                    -> hockey
                                             -> {"first_name": "John", 'last_name': 'Doe', 'age': 28}
                                             -> {"first_name": "Soheil", 'last_name': 'Mat', 'age': 25}
"""

document = {"first_name": "Morteza", 'last_name': 'Matbou', 'age': 25}
document_list = [
    {"first_name": "Morteza", 'last_name': 'Matbou', 'age': 25},
    {"first_name": "Yahya", 'last_name': 'Rezayi', 'age': 29},
]
# player = hockey.insert_one(document)
# print(player.inserted_id)

# The insert_many() method returns a InsertManyResult object, which has a property, inserted_ids,
# that holds the ids of the inserted documents.

# player = hockey.insert_many(document_list)
# print(player.inserted_ids)

# players = hockey.find({'first_name': "John"})

# SELECT COUNT(col_name) AS c FROM table_name WHERE first_name = 'John'
# print(hockey.count_documents({'first_name': "John"}))

# + Insert Multiple Documents, with Specified IDs
# If you do not want MongoDB to assign unique ids for you document, you can specify the _id
# field when you insert the document(s).
# Remember that the values has to be unique. Two documents cannot have the same _id.

document_list_2 = [
    {'_id': 3, 'first_name': "Reza", 'last_name': 'Rezayi', "age": 24},
    {'_id': 4, 'first_name': "Ahmad", 'last_name': 'Ahmadi', "age": 29},
]

# players = hockey.insert_many(document_list_2)
# print(players.inserted_ids)
