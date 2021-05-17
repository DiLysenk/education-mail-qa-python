import pytest
from selenium import webdriver
import allure


@pytest.fixture()
def driver(request):
    browser = webdriver.Chrome()

    failed_tests_count = request.session.testsfailed
    yield browser

    if request.session.testsfailed > failed_tests_count:
        allure.attach(browser.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

    browser.quit()


@allure.epic('AWESOME AUTOTESTS')
@allure.feature('UI TEST')
@allure.story('SEARCH TEST')
def test_python(driver):
    with allure.step('Going to python.org'):
        driver.get('https://www.python.org')

    assert 'Python' in driver.title

    with allure.step('Enterting pycon'):
        elem = driver.find_element_by_name('q')
        elem.send_keys('pycon')

    with allure.step('Clicking GO button'):
        button = driver.find_element_by_xpath('//button[@id="submit"]')
        button.click()

    with allure.step('Make assert'):
        assert 'No results found' in driver.page_source


def test_mail_ru(driver):
    driver.get('https://www.mail.ru')

    auto_button = driver.find_element_by_xpath('//a[@data-testid="news-tabs-tab-item-auto"]')
    auto_button.click()
