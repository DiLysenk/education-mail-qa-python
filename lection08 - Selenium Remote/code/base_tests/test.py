import os
import time
from contextlib import contextmanager

import allure
import pytest
import requests
from selenium.webdriver.common.by import By

from base_tests.base import BaseCase
from utils.decorators import wait


# def test_all_drivers(all_drivers):
#     time.sleep(2)


class TestOne(BaseCase):

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
    def test_search(self, query):
        self.base_page.search(query)
        assert "No results found." not in self.driver.page_source

    def test_search_negative(self):
        self.search_page.search("dasdasdasdasdasdasdasdasdasdas")
        assert "No results found." in self.driver.page_source

    def test_carousel(self):
        self.main_page.click(self.main_page.locators.COMPREHENSIONS, timeout=17)


class TestEvents(BaseCase):

    def test_python_events(self):
        python_events_page = self.main_page.go_to_events('python-events')
        python_events_page.click(python_events_page.locators.EURO_PYTHON_2022)
        assert python_events_page.get_event_location() == 'Dublin, Ireland'

    def test_relative(self):
        introduction = self.main_page.find(self.main_page.locators.INTRODUCTION)
        learn_more = introduction.find_element(*self.main_page.locators.LEARN_MORE_RELATIVE)
        assert learn_more.get_attribute('href') == self.driver.current_url + 'doc/'


class TestDownload(BaseCase):

    def test_download(self, test_dir):
        self.driver.get('https://www.python.org/downloads/release/python-2710/')
        file_name = 'python2710.chm'

        from selenium.webdriver.common.by import By
        self.main_page.click((By.XPATH, f'//a[contains(@href,"{file_name}")]'))

        wait(self.check_download, error=AssertionError, timeout=60, interval=0.1, check=True,
             test_dir=test_dir, file_name=file_name)
        assert os.path.exists(os.path.join(test_dir, file_name))


class TestUpload(BaseCase):

    @pytest.fixture(scope='function')
    def file_path(self, repo_root):
        return os.path.join(repo_root, 'ui', 'test1234567890')

    def test_upload(self, file_path):
        self.driver.get('https://ps.uci.edu/~franklin/doc/file_upload.html')

        input_locator = (By.NAME, 'userfile')
        submit_locator = (By.XPATH, '//input[@type="submit"]')
        input_field = self.main_page.find(input_locator)

        input_field.send_keys(file_path)
        self.main_page.click(submit_locator)


class TestIframe(BaseCase):

    @contextmanager
    def switch_to_frame(self, locator):
        iframe = self.main_page.find(locator)
        self.driver.switch_to.frame(iframe)
        yield
        self.driver.switch_to_default_content()

    @allure.epic('Awesome PyTest framefork')
    @allure.feature('UI tests')
    @allure.story('Switch test')
    def test_iframe(self):
        self.driver.get('http://www.globemoon.net/iframe-ex.html')

        iframe_locator = (By.XPATH, "//iframe[@src='iframe-congrats.html']")

        with self.switch_to_frame(iframe_locator):
            locator = (By.XPATH, "//pre[contains(text(), 'C O N G R A T U L A T I O N S')]")
            print(self.main_page.find(locator).text)

    @contextmanager
    def switch_to_next_window(self, current, close=True):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()

        self.driver.switch_to.window(current)

    @allure.epic('Awesome PyTest framefork')
    @allure.feature('UI tests')
    @allure.story('Switch test')
    def test_new_tab(self):
        current_window = self.driver.current_window_handle

        self.main_page.click(self.main_page.locators.MEMBERSHIP_DRIVE)

        with self.switch_to_next_window(current_window, close=True):
            time.sleep(5)
            assert self.driver.current_url == 'https://www.python.org/psf/membership/'

        time.sleep(5)


class TestFailure(BaseCase):

    @allure.epic('Awesome PyTest framefork')
    @allure.feature('UI tests')
    @allure.story('Failure test')
    def test_failure(self):
        self.driver.get('https://target.my.com')
        self.main_page.find((By.XPATH, '2321321312312'), timeout=1)


class TestLog(BaseCase):

    @allure.epic('Awesome PyTest framefork')
    @allure.feature('UI tests')
    @allure.story('Log test')
    @allure.testcase('https://mail.ru')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.issue('https://jira.com/')
    @allure.description("""
                        We just go to python.org, 
                        then we click events, 
                        then we go to EuroPython 2022 
                        and check its location.
                        Wow... Hmmmm. Sounds good. Lois.
                        """
                        )
    @pytest.mark.UI
    def test_python_events(self):
        self.logger.info('Going to Python events')
        with allure.step('Going to Python events'):
            python_events_page = self.main_page.go_to_events('python-events')
        python_events_page.click(python_events_page.locators.EURO_PYTHON_2022)

        with allure.step('Checking location'):
            assert python_events_page.get_event_location() == 'Dublin, Ireland!'
