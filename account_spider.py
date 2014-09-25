import requests
import json
import base64
from pymongo import MongoClient
class AccountSpider:
    client = MongoClient('localhost', 27017)
    db = client["twitter-spider-database"]
    collection = db.accounts
    def __init__(self):
       secrets_fo = open('secrets.json','r')
       secrets = json.loads(secrets_fo.read())
       secrets_fo.close()
       self.bearer_token = self.__get_bearer_token(base64.b64encode(secrets["twitter_token"]))

    def __get_bearer_token(self, twitter_token):
        headers = {"User-Agent": "Account-Spider", "Authorization": "Basic " + twitter_token,
                 "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
         }
        body = "grant_type=client_credentials"
        r = requests.post('https://api.twitter.com/oauth2/token', headers=headers, data=body)
        return json.loads(r.text)["access_token"]



print AccountSpider().bearer_token;
