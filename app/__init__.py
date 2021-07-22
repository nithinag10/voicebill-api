from flask import Flask
from flask import request, jsonify
import pymongo
from pymongo import MongoClient
import bson
from bson import json_util
from bson.json_util import dumps

import json

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://RFIDpayments:Ff6RfZyRN5arkgvz@payments-ukurt.mongodb.net/test?retryWrites=true&w=majority")
db = client["voice_bill"]
users = db["system_users"]
collection2 = db["billsDemo"]
bills = db["billsDemo"]
@app.route("/fetch", methods=["POST"])
def fetch_user_data():
    inputs = request.get_json(force=True)
    id = inputs["_id"]
    username = inputs["username"]
    data = users.find({"_id": id, "username": username})
    data_list = list(data)
    data_json = dumps(data_list)
    print(data_list == [],type(data),data_list)
    if data_list == []:
        users.insert_one({"_id": id, "username": username})
        data = users.find({"_id": id, "username": username})
        data_list = list(data)
        data_list.append([])
        data_json = dumps(data_list)
        return data_json
    else:
        # if user exists
        data = bills.find({"userId": id})
        # find all the bills with userId equal to the id recieved in the request
        data_list.append(data)
        # append the bills found with the list containing the user data
        data_json = dumps(data_list)
        # convert to json
        return data_json


@app.route("/addbill",methods=['POST'])
def add_bill():
    inputs = request.get_json(force=True)
    customer = inputs["customer"]
    total = inputs["total"]
    items = inputs["items"]
    userId = inputs["userId"]
    bills.insert_one({"customer":customer,"total":total,"items":items,"userId":userId})
    res = bills.find({"customer":customer,"total":total,"items":items,"userId":userId})
    resData = dumps(list(res))
    print(resData)
    return resData


from app import routes

from audio_processing import routes