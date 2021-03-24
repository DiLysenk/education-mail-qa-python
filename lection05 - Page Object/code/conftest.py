from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='http://www.python.org')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    return {'url': url}
