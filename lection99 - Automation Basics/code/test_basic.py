# from selenium.webdriver.common.keys import Keys
import pytest


@pytest.mark.smoke
def test_1():
    assert 1 == 2


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.parametrize('i', list(range(10)))
def test_2(i):
    assert i % 2 == 0


@pytest.mark.regress
def test_3():
    with pytest.raises(ZeroDivisionError):
        assert 1 / 0
