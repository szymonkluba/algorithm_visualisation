import time

from flask_socketio import emit


class Algorithm:
    def __init__(self, array):
        self.array = array
        self.swaps = {}

    def update_display(self, delay=None):
        print(self.swaps)
        emit("update array", self.swaps)
        if delay:
            time.sleep(delay)

    def get_swaps(self, index1, index2, style):
        self.swaps["index1"] = index1
        self.swaps["value1"] = self.array[index1]
        self.swaps["index2"] = index2
        self.swaps["value2"] = self.array[index2]
        self.swaps["style"] = style
        if style == 'regular':
            self.update_display()
        else:
            self.update_display(.000001)

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


class Quicksort(Algorithm):

    name = "Quicksort"

    def __init__(self, array):
        super().__init__(array)

    def algorithm(self):
        def partition(array, begin, end):
            i = begin - 1
            pivot = array[end]
            for j in range(begin, end):
                if array[j] <= pivot:
                    i += 1
                    self.get_swaps(i, j, "current")
                    array[i], array[j] = array[j], array[i]
                    self.get_swaps(i, j, "swapped")
                    self.get_swaps(i, j, "regular")
            self.get_swaps(i + 1, end, "current")
            array[i + 1], array[end] = array[end], array[i + 1]
            self.get_swaps(i + 1, end, "swapped")
            self.get_swaps(i + 1, end, "regular")
            return i + 1

        def quicksort(array, begin, end):
            if begin >= end:
                return

            pivot_index = partition(array, begin, end)
            quicksort(array, begin, pivot_index - 1)
            quicksort(array, pivot_index + 1, end)

        quicksort(self.array, 0, len(self.array) - 1)


class SelectionSort(Algorithm):

    name = "Selection Sort"

    def __init__(self, array):
        super().__init__(array)

    def algorithm(self):
        for i in range(len(self.array) - 1):
            min_index = i
            for j in range(i + 1, len(self.array)):
                self.get_swaps(j, min_index, "current")
                self.get_swaps(j, min_index, "regular")
                if self.array[min_index] > self.array[j]:
                    min_index = j
                    self.get_swaps(j, j, "swapped")
                    self.get_swaps(j, j, "regular")
            self.get_swaps(i, min_index, "current")
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.get_swaps(i, min_index, "swapped")
            self.get_swaps(i, min_index, "regular")
