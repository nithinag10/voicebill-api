from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime
app = Flask(__name__)



client = MongoClient("mongodb+srv://RFIDpayments:Ff6RfZyRN5arkgvz@payments-ukurt.mongodb.net/test?retryWrites=true&w=majority")
db = client["voice_bill"]
collection = db["items"]


@app.route("/fetch", methods=["POST"])
def fetch_user_data():
    inputs = request.get_json(force=True)
    id = inputs["_id"]
    username = inputs["username"]
    data = collection.find({"_id":id, "username":username})
    data_list = list(data)
    data_json = dumps(data_list)
    if data_list == []:
        collection.insert_one({"_id":id, "username":username,"bills":[]})
        data = collection.find({"_id":id,"username":username})
        data_list = list(data)
        data_json = dumps(data_list)
        return data_json
    else:
        return data_json


from audio_processing.routes import *


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)