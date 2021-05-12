from algorithm import Algorithm


class BubbleSort(Algorithm):
    name = "Bubble Sort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    def algorithm(self):
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, len(self.array)):
                if self.array[i - 1] > self.array[i]:
                    self.array[i - 1], self.array[i] = self.array[i], self.array[i - 1]
                    swapped = True
                self.display_updater.update(i - 1, i)


class BubbleSortOptimized(Algorithm):
    name = "Bubble Sort Optimized"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    def algorithm(self):
        swapped = True
        n = len(self.array)
        while swapped:
            if self.stopped:
                break
            swapped = False
            for i in range(1, n):
                if self.stopped:
                    break
                if self.array[i - 1] > self.array[i]:
                    self.array[i - 1], self.array[i] = self.array[i], self.array[i - 1]
                    swapped = True
                self.display_updater.update(i - 1, i)
            n -= 1


class InsertionSort(Algorithm):
    name = "Insertion Sort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    def algorithm(self):
        for i in range(1, len(self.array)):
            current_element = self.array[i]
            current_position = i
            while current_position > 0 and current_element < self.array[current_position - 1]:
                self.array[current_position] = self.array[current_position - 1]
                current_position -= 1
            self.array[current_position] = current_element
            self.display_updater.update(current_position, i)


class Quicksort(Algorithm):
    name = "Quicksort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

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
                array[i], array[j] = array[j], array[i]
                self.display_updater.update(i, j)
        array[i + 1], array[end] = array[end], array[i + 1]
        self.display_updater.update(i + 1, end)
        return i + 1


class SelectionSort(Algorithm):
    name = "Selection Sort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    def algorithm(self):
        for i in range(len(self.array) - 1):
            min_index = i
            for j in range(i + 1, len(self.array)):
                if self.array[min_index] > self.array[j]:
                    min_index = j
                self.display_updater.update(min_index, j)
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.display_updater.update(i, min_index)


class MergeSort(Algorithm):
    name = "Merge Sort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    def algorithm(self, left=None, right=None):

        if left is None:
            left = 0

        if right is None:
            right = len(self.array) - 1

        middle = (left + right) // 2
        if left < right:
            self.algorithm(left, middle)
            self.algorithm(middle + 1, right)
            self.merge(left, middle, middle + 1, right)

    def merge(self, left_begin, left_end, right_begin, right_end):
        i = left_begin
        j = right_begin
        temp = []
        while i <= left_end and j <= right_end:
            self.display_updater.update(i, j)
            if self.array[i] < self.array[j]:
                temp.append(self.array[i])
                i += 1
            else:
                temp.append(self.array[j])
                j += 1
        while i <= left_end:
            self.display_updater.update(i)
            temp.append(self.array[i])
            i += 1
        while j <= right_end:
            self.display_updater.update(j)
            temp.append(self.array[j])
            j += 1
        j = 0
        for i in range(left_begin, right_end + 1):
            self.array[i] = temp[j]
            j += 1
            self.display_updater.update(i)
