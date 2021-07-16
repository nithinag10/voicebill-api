from flask import Flask
from pymongo import MongoClient
from datetime import datetime
app = Flask(__name__)


client = MongoClient("mongodb+srv://RFIDpayments:Ff6RfZyRN5arkgvz@payments-ukurt.mongodb.net/test?retryWrites=true&w=majority")
db = client["voice_bill"]
collection = db["items"]


@app.route('/')
def homepage():
    return "hello macha its working"

from audio_processing.routes import process_input

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)