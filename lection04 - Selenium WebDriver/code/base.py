import pytest
import basic_locators
from selenium.common.exceptions import StaleElementReferenceException

CLICK_RETRY = 3


class BaseCase:
    driver = None
    config = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

    def find(self, locator):
        return self.driver.find_element(*locator)

    def search(self, query):
        search = self.find(basic_locators.QUERY_LOCATOR)
        search.clear()
        search.send_keys(query)
        # go = self.find(basic_locators.GO_LOCATOR)
        self.click(basic_locators.GO_LOCATOR)

    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator)
                if i < 2:
                    self.driver.refresh()
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

