import os
import time

import pytest
from selenium.webdriver.common.by import By

from base_tests.base import BaseCase
from utils.decorators import wait


@pytest.mark.skip("SKIP")
def test_all_drivers(all_drivers):
    time.sleep(2)


class TestOne(BaseCase):
    @pytest.mark.skip("SKIP")
    def test_title(self):
        assert "Python" in self.driver.title

    @pytest.mark.parametrize(
        'query',
        [
            pytest.param(
                'pycon'
            ),
            pytest.param(
                'python'
            ),
        ]
    )
    @pytest.mark.skip("SKIP")
    def test_search(self, query):
        self.base_page.search(query)
        assert "No results found." not in self.driver.page_source

    @pytest.mark.skip("SKIP")
    def test_search_negative(self):
        self.search_page.search("dasdasdasdasdasdasdasdasdasdas")
        assert "No results found." in self.driver.page_source

    @pytest.mark.skip("SKIP")
    def test_carousel(self):
        self.main_page.click(self.main_page.locators.COMPREHENSIONS, timeout=17)


class TestEvents(BaseCase):

    @pytest.mark.skip("SKIP")
    def test_python_events(self):
        python_events_page = self.main_page.go_to_events('python-events')
        python_events_page.click(python_events_page.locators.EURO_PYTHON_2022)
        assert python_events_page.get_event_location() == 'Dublin, Ireland'

    @pytest.mark.skip("SKIP")
    def test_relative(self):
        introduction = self.main_page.find(self.main_page.locators.INTRODUCTION)
        learn_more = introduction.find_element(*self.main_page.locators.LEARN_MORE_RELATIVE)
        assert learn_more.get_attribute('href') == self.driver.current_url + 'doc/'


class TestDownload(BaseCase):

    @staticmethod
    def check_download(temp_dir, file_name):
        for f in os.listdir(temp_dir):
            if f.endswith('.crdownload'):
                return False

        assert file_name in os.listdir(temp_dir)
        return True

    @pytest.mark.skip("SKIP")
    def test_download(self, temp_dir):
        self.driver.get('https://www.python.org/downloads/release/python-2710/')
        file_name = 'python2710.chm'

        from selenium.webdriver.common.by import By
        self.main_page.click((By.XPATH, f'//a[contains(@href,"{file_name}")]'))

        wait(self.check_download, error=AssertionError, timeout=5, interval=0.1, check=True,
             temp_dir=temp_dir, file_name=file_name)
        assert os.path.exists(os.path.join(temp_dir, file_name))


class TestUpload(BaseCase):

    @pytest.fixture(scope='function')
    def file_path(self, repo_root):
        return os.path.join(repo_root, 'ui', 'test1234567890')

    @pytest.mark.skip("SKIP")
    def test_upload(self, file_path):
        self.driver.get('https://ps.uci.edu/~franklin/doc/file_upload.html')

        input_locator = (By.NAME, 'userfile')
        submit_locator = (By.XPATH, '//input[@type="submit"]')
        input_field = self.main_page.find(input_locator)

        input_field.send_keys(file_path)
        self.main_page.click(submit_locator)
