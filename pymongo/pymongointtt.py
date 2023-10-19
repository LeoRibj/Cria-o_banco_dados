import datetime
import pprint

import pymongo as pym

client = pym.MongoClient("mongodb+srv://ManigoldoCR:Leo984237785@cluster0.xfpuzca.mongodb.net/?retryWrites=true&w=majority")

db = client.tb

collection = db.clientes
#print(db.clientes)

post = [{
    "nome": "Leo",
    "cpf": "00022288825",
    "enderço": ["rua lll","bairro jjj"],
    "balanço": "5000",
    "contas": ["00001","00002"],
    "tags" : ["python","mongodb"]
},{
    "nome": "Duda",
    "cpf": "66655544452",
    "enderço": ["rua lll", "bairro jjj"],
    "balanço": "5000",
    "contas": "55500",
    "tags": ["python", "mongodb"]
}]



posts = db.posts
post_id = posts.insert_many(post)
print(post_id)

print(db.posts.find_one({"nome": "Duda"}))


