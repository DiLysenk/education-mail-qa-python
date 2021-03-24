import pytest
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.search_page import SearchPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def search_page(driver):
    return SearchPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = webdriver.Chrome(executable_path='')
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.close()
