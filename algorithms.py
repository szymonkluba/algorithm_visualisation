import time

from flask_socketio import emit

from display_update import DisplayUpdate


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
                display_updater = DisplayUpdate(self.array, i - 1, i)
                if self.array[i - 1] > self.array[i]:
                    self.array[i - 1], self.array[i] = self.array[i], self.array[i - 1]
                    swapped = True
                display_updater.update()


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
                display_updater = DisplayUpdate(self.array, i - 1, i)
                if self.array[i - 1] > self.array[i]:
                    self.array[i - 1], self.array[i] = self.array[i], self.array[i - 1]
                    swapped = True
                display_updater.update()
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
                self.array[current_position] = self.array[current_position - 1]
                current_position -= 1
            display_updater = DisplayUpdate(self.array, current_position, i)
            self.array[current_position] = current_element
            display_updater.update()


class Quicksort(Algorithm):
    name = "Quicksort"

    def __init__(self, array):
        super().__init__(array)

    def algorithm(self, array=None, begin=0, end=0):
        if not array:
            array = self.array
            end = len(self.array) - 1
        if begin >= end:
            return

        pivot_index = self.partition(array, begin, end)
        self.algorithm(array, begin, pivot_index - 1)
        self.algorithm(array, pivot_index + 1, end)

    def partition(self, array, begin, end):
        i = begin - 1
        pivot = array[end]
        for j in range(begin, end):
            if array[j] <= pivot:
                i += 1
                display_updater = DisplayUpdate(self.array, i, j)
                array[i], array[j] = array[j], array[i]
                display_updater.update()
        display_updater = DisplayUpdate(self.array, i + 1, end)
        array[i + 1], array[end] = array[end], array[i + 1]
        display_updater.update()
        return i + 1


class SelectionSort(Algorithm):
    name = "Selection Sort"

    def __init__(self, array):
        super().__init__(array)

    def algorithm(self):
        for i in range(len(self.array) - 1):
            min_index = i
            for j in range(i + 1, len(self.array)):
                display_updater = DisplayUpdate(self.array, min_index, j)
                if self.array[min_index] > self.array[j]:
                    min_index = j
                display_updater.update()
            display_updater = DisplayUpdate(self.array, i, min_index)
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            display_updater.update()