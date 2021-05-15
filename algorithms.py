from algorithm import Algorithm

""" Class for Bubble Sort """


class BubbleSort(Algorithm):
    name = "Bubble Sort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    def algorithm(self):
        swapped = True
        while swapped:
            if self.stopped:
                break
            swapped = False
            for i in range(1, len(self.array)):
                if self.stopped:
                    break
                if self.array[i - 1] > self.array[i]:
                    self.array[i - 1], self.array[i] = self.array[i], self.array[i - 1]
                    swapped = True
                self.display_updater.update(i - 1, i)


""" Class for optimized Bubble sort """


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


""" Class for Insertion Sort """


class InsertionSort(Algorithm):
    name = "Insertion Sort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    def algorithm(self):
        for i in range(1, len(self.array)):
            if self.stopped:
                break
            current_element = self.array[i]
            current_position = i
            while current_position > 0 and current_element < self.array[current_position - 1]:
                self.display_updater.update(current_position, current_position - 1)
                if self.stopped:
                    break
                self.array[current_position] = self.array[current_position - 1]
                current_position -= 1
            self.array[current_position] = current_element
            self.display_updater.update(current_position, i)


""" Class for Quicksort """


class Quicksort(Algorithm):
    name = "Quicksort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    def algorithm(self, begin=0, end=None):
        if not end:
            end = len(self.array) - 1
        if begin >= end:
            return
        if self.stopped:
            return

        pivot_index = self.partition(begin, end)
        self.algorithm(begin, pivot_index - 1)
        self.algorithm(pivot_index + 1, end)

    def partition(self, begin, end):
        if self.stopped:
            return
        i = begin - 1
        pivot = self.array[end]
        for j in range(begin, end):
            if self.stopped:
                break
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.display_updater.update(i, j)
        self.array[i + 1], self.array[end] = self.array[end], self.array[i + 1]
        self.display_updater.update(i + 1, end)
        return i + 1


""" Class for Selection Sort """


class SelectionSort(Algorithm):
    name = "Selection Sort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    def algorithm(self):
        for i in range(len(self.array) - 1):
            if self.stopped:
                break
            min_index = i
            for j in range(i + 1, len(self.array)):
                if self.stopped:
                    break
                if self.array[min_index] > self.array[j]:
                    min_index = j
                self.display_updater.update(min_index, j)
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.display_updater.update(i, min_index)


""" Class for Merge Sort """


class MergeSort(Algorithm):
    name = "Merge Sort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    def algorithm(self, left=None, right=None):

        if self.stopped:
            return

        if left is None:
            left = 0

        if right is None:
            right = len(self.array) - 1

        middle = (left + right) // 2
        if left < right:
            self.algorithm(left, middle)
            self.algorithm(middle + 1, right)
            self.merge(left, middle, middle + 1, right)

    # Helper method for merging subarray
    def merge(self, left_begin, left_end, right_begin, right_end):
        if self.stopped:
            return
        i = left_begin
        j = right_begin
        temp = []
        while i <= left_end and j <= right_end:
            if self.stopped:
                break
            self.display_updater.update(i, j)
            if self.array[i] < self.array[j]:
                temp.append(self.array[i])
                i += 1
            else:
                temp.append(self.array[j])
                j += 1
        while i <= left_end:
            if self.stopped:
                break
            self.display_updater.update(i)
            temp.append(self.array[i])
            i += 1
        while j <= right_end:
            if self.stopped:
                break
            self.display_updater.update(j)
            temp.append(self.array[j])
            j += 1
        j = 0
        for i in range(left_begin, right_end + 1):
            if self.stopped:
                break
            self.array[i] = temp[j]
            j += 1
            self.display_updater.update(i)


""" Class for Heap Sort """


class HeapSort(Algorithm):
    name = "Heap Sort"

    def __init__(self, array, socket):
        super().__init__(array, socket)

    # Helper method for building heap
    def build_heap(self, size, index):
        if self.stopped:
            return
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        print(self.array)
        if left < size and self.array[largest] < self.array[left]:
            largest = left

        print(self.array)
        if right < size and self.array[largest] < self.array[right]:
            largest = right

        if largest != index:
            self.display_updater.update(index, largest)
            print(self.array)
            self.array[index], self.array[largest] = self.array[largest], self.array[index]
            self.build_heap(size, largest)

    def algorithm(self):
        if self.stopped:
            return
        size = len(self.array)

        for i in range(size // 2 - 1, -1, -1):
            if self.stopped:
                break
            self.build_heap(size, i)

        for i in range(size - 1, 0, -1):
            if self.stopped:
                break
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.display_updater.update(i, 0)
            print(self.array)
            self.build_heap(i, 0)
