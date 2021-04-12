from ui.pages.base_page import BasePage
from ui.locators.locators_web import TitleListPageLocators
from ui.locators.locators_mw import TitleListPagePageMWLocators
from selenium.webdriver.common.by import By
import time
import allure


class TitleListPage(BasePage):
    locators = TitleListPageLocators()

