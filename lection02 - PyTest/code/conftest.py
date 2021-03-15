import sys


def is_master(config):
    if hasattr(config, 'workerinput'):
        return False
    return True


def pytest_configure(config):
    if is_master(config):
        print('This is configure hook on MASTER\n')
    else:
        sys.stderr.write(f'This is configure hook on WORKER{config.workerinput["workerid"]}\n')


def pytest_unconfigure(config):
    if is_master(config):
        print('This is unconfigure hook on MASTER\n')
    else:
        sys.stderr.write(f'This is unconfigure hook on WORKER{config.workerinput["workerid"]}\n')


def pytest_addoption(parser):
    parser.addoption('--env', type=str, default='prod')


def pytest_generate_tests(metafunc):
    if metafunc.function.__name__ == 'test_params_by_hook':
        if metafunc.config.option.env == 'prod':
            metafunc.parametrize('i', [1, 2, 3, 4])
        elif metafunc.config.option.env == 'test':
            metafunc.parametrize('i', [5, 6, 7, 8])












