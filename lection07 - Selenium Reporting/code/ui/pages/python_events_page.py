from ui.pages.base_page import BasePage
from ui.locators.pages_locators import PythonEventsPageLocators


class PythonEventsPage(BasePage):
    url = 'https://www.python.org/events/python-events'

    locators = PythonEventsPageLocators()

    def get_event_location(self):
        return self.find(self.locators.LOCATION).text

