import random
from contextlib import contextmanager


class Random:

    def __enter__(self):
        print('Entering...')
        return random.randint(0, 100)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting...')


with Random() as r:
    print(r)
    print('Inside...')


with Random() as r:
    print(r)
    print('Inside 2...')


@contextmanager
def random_test():
    print('Entering...')
    yield random.randint(0, 100)
    print('Exiting...')


with random_test() as r:
    print(r)
    print('Inside...')
