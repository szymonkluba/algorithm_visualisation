import time


class DisplayUpdate:

    def __init__(self, array, socket):
        self.array = array
        self.socket = socket
        self.index1 = None
        self.index2 = None
        self.data = {}
        self.delay = self.set_delay()

    def get_data(self):
        self.data["array"] = self.array
        if self.index1 is not None:
            self.data["index1"] = self.index1
        if self.index2 is not None:
            self.data["index2"] = self.index2

    def update(self, index1=None, index2=None):
        self.index1 = index1
        self.index2 = index2
        self.get_data()
        self.socket.emit("update array", self.data)
        time.sleep(self.delay)

    def set_delay(self):
        return .0001 * (10000 / len(self.array))
