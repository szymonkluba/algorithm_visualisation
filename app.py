from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from algorithms import BubbleSort
from helpers import generate_random_array

app = Flask(__name__)
socketio = SocketIO(app)

array = []

available_algorithms = {
    "bubble_sort": BubbleSort,
}


@app.route('/')
def index():
    algorithms = []
    for k, v in available_algorithms.items():
        algorithms.append({"key": k, "name": v})
    return render_template("index.html", algorithms=algorithms)


@socketio.on("generate array")
def generate_array():
    global array
    array = generate_random_array()
    emit("generated array", {"array": array})


@socketio.on("run algorithm")
def run_algorithm(data):
    print(array)
    print(data)
    algorithm = available_algorithms[data["algorithm"]](array)
    algorithm.run()



if __name__ == '__main__':
    socketio.run(app)
