import time

""" Display updater class """


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

        # Include indexes of bars to be highlighted
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
        # Delay depends on array size
        return 1 / len(self.array)
