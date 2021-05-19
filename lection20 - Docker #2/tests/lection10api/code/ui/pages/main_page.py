from ui.pages.base_page import BasePage
from ui.locators.pages_locators import MainPageLocators


class MainPage(BasePage):
    url = 'https://education.mail.ru/feed/'

    locators = MainPageLocators()

    def is_opened(self):
        super(MainPage, self).is_opened()
        return self.find(self.locators.FEED)
