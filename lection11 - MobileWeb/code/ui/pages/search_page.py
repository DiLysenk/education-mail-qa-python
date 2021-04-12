from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators.locators_web import SearchPageLocators
from ui.locators.locators_mw import SearchPagePageMWLocators
import allure


class SearchPage(BasePage):
    locators = SearchPageLocators()


