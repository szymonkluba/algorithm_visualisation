from multiprocessing import Pool

from flask import Flask, render_template
from flask_socketio import SocketIO

from helpers import generate_random_array
from settings import available_algorithms

app = Flask(__name__)
socketio = SocketIO(app)

array = []
algorithm = None


@app.route('/')
def index():
    algorithms = []
    for k, v in available_algorithms.items():
        algorithms.append({"key": k, "name": v.get_name()})
    return render_template("index.html", algorithms=algorithms)


@socketio.on("generate array")
def generate_array(data):
    global array
    array = generate_random_array(int(data["size"]))
    socketio.emit("generated array", {"array": array})


@socketio.on("run algorithm")
def run_algorithm(data):
    global algorithm
    algorithm = available_algorithms[data["algorithm"]](array, socketio)
    algorithm.run_algorithm()


@socketio.on("stop algorithm")
def stop_algorithm():
    global algorithm
    if algorithm:
        algorithm.stopped = True


if __name__ == '__main__':
    socketio.run(app)
