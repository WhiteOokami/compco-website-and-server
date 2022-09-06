import pymongo
from bson.json_util import dumps
import re
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"


myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase"]
userCol = mydb["users"]
compCol = mydb["competitions"]

def addUser(username, password):
    #force lowercase
    username = username.lower();
    userInfo = { "username": username, "password": password }
    x = userCol.insert_one(userInfo)

def getUser(username):
    username = username.lower();
    user = userCol.find_one({"username": username})
    print(user)
    return user

def addSearch():
    print("hi")

def getAll():
    cursor =  mycol.find()
    docs = list(cursor)
    docs = dumps(docs, indent=2, sort_keys=True)

def getCompetitionsWithName(name):
    comps = compCol.find({"name":re.compile(name, re.IGNORECASE)},{})
    comps = dumps(comps)
    print(comps)
    return comps