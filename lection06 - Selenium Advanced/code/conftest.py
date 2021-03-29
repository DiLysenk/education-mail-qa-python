from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='http://www.python.org')
    parser.addoption('--browser', default='chrome')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    return {'url': url, 'browser': browser}


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))
