import pytest


@pytest.mark.parametrize('i', list(range(100)))
def test(i):
    assert i % 2 == 0
