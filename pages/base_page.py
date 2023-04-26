from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
import math, time, random
from selenium.webdriver.support.wait import WebDriverWait
from .locators import LoginPageLocators, MainPageLocators, ProfilePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    """Переход на таб "Пользователи" в профиле"""
    def go_to_stewards(self):
        self.browser.find_element(*MainPageLocators.PROFILE_BUTTON).click()
        self.browser.find_element(*ProfilePageLocators.TAB_USERS).click()
        self.browser.find_element(*ProfilePageLocators.ADD_USER_BUTTON).click()

    """Проверяем, что элемента нет на странице"""
    def is_not_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    """Генератор букв"""
    def cyrillic_letter_generation(self, length):
        letters = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяЁё'
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

