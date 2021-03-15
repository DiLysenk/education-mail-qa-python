import random
import sys

import pytest


@pytest.fixture(scope='function', params=list(range(10)))
def fixture(request):
    if request.param > 5:
        return 10

    elif request.param < 3:
        return 5

    else:
        return 0


@pytest.fixture(scope='session')
def session_fixture():
    return random.randint(0, 100)


@pytest.mark.parametrize('i', list(range(0, 10)))
def test(i, session_fixture):
    sys.stderr.write(str(session_fixture) + '\n')


def test_params_by_hook(i):
    print(i)
    assert i == 0

