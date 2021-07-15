from app import app
from flask import jsonify , request


@app.errorhandler(404)
def handle():
    return "Error ide Macha"

@app.route("/")
def home():
    return "Machas its working!!"
