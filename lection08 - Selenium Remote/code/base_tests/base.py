import os

import pytest
import requests
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.search_page import SearchPage


class BaseCase:

    def check_download(self, test_dir, file_name):
        if selenoid := self.config['selenoid']:
            res = requests.get(f'{selenoid}/download/{self.driver.session_id}/{file_name}')
            if res.status_code == 404:
                return False

            with open(os.path.join(test_dir, file_name), 'wb') as f:
                f.write(res.content)
            return True
        else:
            for f in os.listdir(test_dir):
                if f.endswith('.crdownload'):
                    return False

            assert file_name in os.listdir(test_dir)
            return True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.search_page: SearchPage = request.getfixturevalue('search_page')

        self.logger.debug('Initial setup done!')
