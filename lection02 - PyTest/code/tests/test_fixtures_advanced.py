import pytest

import random


@pytest.fixture(scope='session')
def session_fixture():
    r = random.randint(0, 100)
    print(r)
    return r


@pytest.fixture(scope='function')
def func_fixture1(session_fixture):
    return session_fixture // 2


@pytest.fixture(scope='function')
def func_fixture2(session_fixture):
    return session_fixture // 5


def test(func_fixture1):
    print(func_fixture1)


def test2(func_fixture2):
    print(func_fixture2)


@pytest.fixture()
def auto_fixture():
    print('AUTO')
    return 'AUTO'


def test1(request):
    print(request.getfixturevalue('auto_fixture'))
