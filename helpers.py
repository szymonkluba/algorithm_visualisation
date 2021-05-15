from random import randint


def generate_random_array(size):
    return [randint(10, 99) for _ in range(size)]
