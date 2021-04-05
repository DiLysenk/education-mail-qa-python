import time

import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By

from ui.fixtures import get_driver
from ui.pages.base_page import BasePage


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = get_driver(config['browser'], '')
    driver.get(config['url'])

    login_page = LoginPage(driver)
    login_page.login(*credentials)

    cookies = driver.get_cookies()
    driver.quit()

    return cookies


@pytest.fixture(scope='session')
def credentials():
    with open('/tmp/user', 'r') as f:
        user = f.readline().strip()
        password = f.readline().strip()

    return user, password


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver =driver
        self.config = config
        self.logger = logger

        self.login_page = LoginPage(driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.main_page = MainPage(driver)


class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        self.login_page.login(*credentials)

        time.sleep(5)

    def test_invalid_login(self):
        self.login_page.login('123', '456')

        time.sleep(5)


class TestLK(BaseCase):

    def test_lk1(self):
        time.sleep(5)

    def test_lk2(self):
        time.sleep(5)


class LoginPage(BasePage):
    url = 'https://education.mail.ru/'

    def login(self, user, password):
        self.click((By.CLASS_NAME, 'enter-item'))
        self.find((By.ID, 'id_login_email')).send_keys(user)
        self.find((By.ID, 'id_login_password')).send_keys(password)
        self.click((By.XPATH, '//form[@id="popup-login-form"]//button[@type="submit"]'))

        time.sleep(5)


class MainPage(BasePage):
    url = 'https://education.mail.ru/feed/'