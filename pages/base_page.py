from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
import math, time
from selenium.webdriver.support.wait import WebDriverWait
from .locators import LoginPageLocators, MainPageLocators, ProfilePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def go_to_stewards(self):
        self.browser.find_element(*MainPageLocators.PROFILE_BUTTON).click()
        self.browser.find_element(*ProfilePageLocators.TAB_USERS).click()
        self.browser.find_element(*ProfilePageLocators.ADD_USER_BUTTON).click()


