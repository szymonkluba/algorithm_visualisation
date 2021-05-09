from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    socketio.run(app)
