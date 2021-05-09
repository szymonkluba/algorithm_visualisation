from random import randint


def generate_random_array():
    return [randint(5, 300) for _ in range(200)]
