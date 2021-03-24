from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, 'q')
    GO_LOCATOR = (By.ID, 'submit')


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (By.XPATH, '//code/span[@class="comment" and contains(text(), "comprehensions")]')


class SearchPageLocators(BasePageLocators):
    pass
