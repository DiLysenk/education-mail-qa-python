from ui.pages.base_page import BasePage
from ui.locators.locators_web import LoginLocators
from ui.locators.locators_mw import LoginPageMWLocators
import allure


class LoginPage(BasePage):
    locators = LoginLocators()
