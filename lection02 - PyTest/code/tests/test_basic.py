import pytest


def test():
    assert {1: 1} == {2: 2}


def check_zero_division(a, b):
    assert a / b


class Test:

    def test(self):
        assert 1 != 2

    def test_negative(self):
        with pytest.raises(ZeroDivisionError):
            check_zero_division(1, 0)
            pytest.fail(msg='No ZeroDivisionError error occured')
