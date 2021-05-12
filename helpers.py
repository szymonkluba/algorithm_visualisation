from random import randint


def generate_random_array(size):
    return [randint(5, 300) for _ in range(size)]
