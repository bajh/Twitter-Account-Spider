import requests
from pymongo import MongoClient
class AccountSpider:
    client = MongoClient('localhost', 27017)
    db = client["twitter-spider-database"]
    collection = db.accounts
    def __init__(self):
       secrets_fo = open('secrets.json','r')
       secrets = secrets_fo.read()
       secrets_fo.close()
       print secrets
     #  r= requests.get('http://docs.python-requests.org/en/latest/')

AccountSpider()
