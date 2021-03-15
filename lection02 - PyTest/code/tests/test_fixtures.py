import pytest

import random


@pytest.fixture(scope='function')
def func_fixture():
    print('Entering..')
    yield random.randint(0, 100)
    print('Exiting...')


@pytest.fixture(scope='class')
def class_fixture():
    yield random.randint(0, 100)


@pytest.fixture(scope='session')
def session_fixture():
    yield random.randint(0, 100)


def test1(func_fixture, session_fixture):
    print(func_fixture, session_fixture)


def test2(func_fixture, session_fixture):
    print(func_fixture, session_fixture)


class Test:

    def test1(self, func_fixture, class_fixture, session_fixture):
        print(func_fixture, class_fixture, session_fixture)

    def test2(self, func_fixture, class_fixture, session_fixture):
        print(func_fixture, class_fixture, session_fixture)

