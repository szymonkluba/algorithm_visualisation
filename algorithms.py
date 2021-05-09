import time

from flask_socketio import emit


class Algorithm:
    def __init__(self, array):
        self.array = array
        self.swaps = {}

    def update_display(self):
        emit("update array", self.swaps)
        time.sleep(.0000001)

    def get_swaps(self, index1, index2, style):
        self.swaps["index1"] = index1
        self.swaps["value1"] = self.array[index1]
        if index2:
            self.swaps["index2"] = index2
            self.swaps["value2"] = self.array[index2]
        self.swaps["style"] = style
        self.update_display()

    def run(self):
        self.algorithm()

    @classmethod
    def get_name(cls):
        return cls.name


class BubbleSort(Algorithm):

    name = "Bubble Sort"

    def __init__(self, array):
        super().__init__(array)

    def algorithm(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, len(self.array)):
                self.get_swaps(i - 1, i, "current")
                if self.array[i - 1] > self.array[i]:
                    self.array[i - 1], self.array[i] = self.array[i], self.array[i - 1]
                    self.get_swaps(i - 1, i, "swapped")
                    swapped = True
                self.get_swaps(i - 1, i, "regular")


class BubbleSortOptimized(Algorithm):

    name = "Bubble Sort Optimized"

    def __init__(self, array):
        super().__init__(array)

    def algorithm(self):
        swapped = True
        n = len(self.array)
        while swapped:
            swapped = False
            for i in range(1, n):
                self.get_swaps(i - 1, i, "current")
                if self.array[i - 1] > self.array[i]:
                    self.array[i - 1], self.array[i] = self.array[i], self.array[i - 1]
                    self.get_swaps(i - 1, i, "swapped")
                    swapped = True
                self.get_swaps(i - 1, i, "regular")
            n -= 1


class InsertionSort(Algorithm):

    name = "Insertion Sort"

    def __init__(self, array):
        super().__init__(array)

    def algorithm(self):
        for i in range(1, len(self.array)):
            current_element = self.array[i]
            current_position = i
            while current_position > 0 and current_element < self.array[current_position - 1]:
                self.get_swaps(current_position - 1, current_position, "current")
                self.array[current_position] = self.array[current_position - 1]
                self.get_swaps(current_position - 1, current_position, "swapped")
                self.get_swaps(current_position - 1, current_position, "regular")
                current_position -= 1
            self.get_swaps(current_position, i, "current")
            self.array[current_position] = current_element
            self.get_swaps(current_position, i, "swapped")
            self.get_swaps(current_position, i, "regular")
