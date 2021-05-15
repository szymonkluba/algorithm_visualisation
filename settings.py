from algorithms import BubbleSort, BubbleSortOptimized, InsertionSort, Quicksort, SelectionSort, MergeSort, HeapSort

""" Dictionary stores the classes to be called when algorithm is selected. To extend the app with new algorithm it just 
has to be implemented as new class and added to this dictionary."""
available_algorithms = {
    "bubble_sort": BubbleSort,
    "bubble_sort_optimized": BubbleSortOptimized,
    "insertion_sort": InsertionSort,
    "quicksort": Quicksort,
    "selection_sort": SelectionSort,
    "merge_sort": MergeSort,
    "heap_sort": HeapSort,
}