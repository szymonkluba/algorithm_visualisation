import time

from flask_socketio import emit


class DisplayUpdate:

    def __init__(self, array, index1=None, index2=None):
        self.array = array
        self.index1 = index1
        self.index2 = index2
        self.data = {}

    def get_data(self):
        self.data["array"] = self.array
        if self.index1 is not None:
            self.data["index1"] = self.index1
        if self.index2 is not None:
            self.data["index2"] = self.index2

    def update(self):
        self.get_data()
        emit("update array", self.data)
        time.sleep(.01)