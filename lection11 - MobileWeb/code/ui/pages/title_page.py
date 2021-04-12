from ui.pages.base_page import BasePage
from ui.locators.locators_web import TitlePageLocators
from ui.locators.locators_mw import TitlePagePageMWLocators
import allure


class TitlePage(BasePage):
    locators = TitlePageLocators()
