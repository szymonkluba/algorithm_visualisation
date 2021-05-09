import time

from flask_socketio import emit


class Algorithm:
    def __init__(self, name, array):
        self.array = array
        self.name = name
        self.swaps = {}

    def update_display(self):
        emit("update array", self.swaps)
        time.sleep(.001)

    def get_swaps(self, index, style):
        self.swaps["index1"] = index - 1
        self.swaps["value1"] = self.array[index - 1]
        self.swaps["index2"] = index
        self.swaps["value2"] = self.array[index]
        self.swaps["style"] = style
        self.update_display()

    def run(self):
        self.algorithm()


class BubbleSort(Algorithm):
    def __init__(self, array):
        super().__init__("BubbleSort", array)

    def algorithm(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, len(self.array)):
                self.get_swaps(i, "current")
                if self.array[i - 1] > self.array[i]:
                    self.array[i - 1], self.array[i] = self.array[i], self.array[i - 1]
                    self.get_swaps(i, "swapped")
                    swapped = True
                self.get_swaps(i, "regular")
