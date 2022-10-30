import pymongo
client = pymongo.MongoClient("mongodb+srv://balaji_ch:Automotive@cluster0.j629idg.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"sudhanshu",
    "emailid":"balau2gmail.com",
    "surname":"cheruku"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)