from flask import Flask, jsonify, make_response
import time

app = Flask(__name__)

MESSAGE = {
    "message": "Automate all the things!",
    "timestamp": round(time.time()*1000)
}

@app.route("/")
def hello_from_root():
    return jsonify(MESSAGE)

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
