from multiprocessing import Pool

from flask import Flask, render_template
from flask_socketio import SocketIO

from algorithm import Algorithm
from helpers import generate_random_array
from settings import available_algorithms

# Initialize Flask app
app = Flask(__name__)
# Initialize app with sockets
socketio = SocketIO(app)

# Initialize global array
array = []
# Initialize global variable for instance of Algorithm class
algorithm: Algorithm = None


@app.route('/')
def index():
    algorithms = []
    # Initialize dictionary of keys and algorithm names for <select>
    for k, v in available_algorithms.items():
        algorithms.append({"key": k, "name": v.get_name()})
    return render_template("index.html", algorithms=algorithms)


""" Event generating new random array """


@socketio.on("generate array")
def generate_array(data):
    global array
    # Generate random array
    array = generate_random_array(int(data["size"]))
    socketio.emit("generated array", {"array": array})


""" Event starting algorithm """


@socketio.on("run algorithm")
def run_algorithm(data):
    global algorithm
    try:
        algorithm = available_algorithms[data["algorithm"]](array, socketio)
        algorithm.run_algorithm()
    except KeyError:
        socketio.emit("choose algorithm")


""" Event stopping algorithm """


@socketio.on("stop algorithm")
def stop_algorithm():
    global algorithm
    if algorithm:
        algorithm.stopped = True


if __name__ == '__main__':
    socketio.run(app)
