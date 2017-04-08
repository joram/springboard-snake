import json

from flask import Flask, request

from move import move
from start import start


app = Flask(__name__)


def log_request(request):
    print request.method, request.path


@app.route("/", methods=["GET"])
def handle_index():
    log_request(request)
    return "Hello world I am a snake."


@app.route("/start", methods=["POST"])
def handle_start():
    log_request(request)
    params = json.loads(request.data)

    response = start(params)

    return json.dumps(response)


@app.route("/move", methods=["POST"])
def handle_move():
    log_request(request)
    params = json.loads(request.data)

    response = move(params)

    return json.dumps(response)
