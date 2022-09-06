import pymongo
client = pymongo.MongoClient("mongodb+srv://harisalian31:Vihan1234@hari.vd41ham.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"hari",
    "email":"hpsalia",
    "surname":"salian"
}
db1 = client ['mongotest']
coll = db1['test']
coll.insert_one(d)