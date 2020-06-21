from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.BankAPI

users = db["Users"]

def UserExists(username):
    if users.find({"Username": username}).count()==0:
        return False
    else:
        return True

class Register(Resource):

    def post(self):
        postedData = request.get_json()
        
        username = postedData["username"]
        password = postedData["password"]

        if UserExists(username):
            retJson = {
                "status": "301",
                "msg": "Invalid Username"
            }

            return retJson
        
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
        
        users.insert({
            "Username": username,
            "Password": hashed_pw,
            "Own": 0,
            "Debt":0
        })

        retJson = {
            "status": 200,
            "msg": "You successfully signed up for the API"
        }

        return jsonify(retJson)

def verifyPw(username,password):
    if not UserExists(username):
        return False
    
    hashed_pw = users.find({
        "Username":username
    })[0]["Password"]

    if bcrypt.hashed_pw(password.encode('utf9'),hashed_pw) == hashed_pw:
        return True
    else:
        return False



