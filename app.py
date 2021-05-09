from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit

from helpers import generate_random_array

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return render_template("index.html")


@socketio.on("generate array")
def generate_array():
    emit("generated array", {"array": generate_random_array()})


if __name__ == '__main__':
    socketio.run(app)
