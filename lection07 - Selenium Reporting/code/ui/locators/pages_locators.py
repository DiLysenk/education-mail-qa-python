from selenium.webdriver.common.by import By


class BasePageLocators:
    BASE_PAGE_LOADED_LOCATOR = ''

    QUERY_LOCATOR = (By.NAME, 'q')
    GO_LOCATOR = (By.ID, 'submit')


class MainPageLocators(BasePageLocators):
    COMPREHENSIONS = (By.XPATH, '//code/span[@class="comment" and contains(text(), "comprehensions")]')

    EVENTS_BUTTON = (By.XPATH, '//li[@id="events"]/a[@href="/events/"]')
    EVENTS_LINK_TEMPLATE = (By.XPATH, '//li[@id="events"]//a[@href="/events/{}"]')

    INTRODUCTION = (By.CSS_SELECTOR, 'div.introduction')
    LEARN_MORE_RELATIVE = (By.CSS_SELECTOR, 'a.readmore')

    MEMBERSHIP_DRIVE = (By.XPATH, '//a[@href="https://www.python.org/psf/membership/"]')


class SearchPageLocators(BasePageLocators):
    pass


class PythonEventsPageLocators(BasePageLocators):
    EURO_PYTHON_2022 = (By.XPATH, '//a[contains(text(), "EuroPython 2022")]')
    LOCATION = (By.CLASS_NAME, 'single-event-location')
