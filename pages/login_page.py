from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def authorization(self, url, login, password):
        self.browser.get(url)
        self.browser.implicitly_wait(30)
        self.browser.find_element(*LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        self.browser.find_element(*LoginPageLocators.LOGIN_CODE_VERIFICATION_NUMBER1).send_keys(1)
        self.browser.find_element(*LoginPageLocators.LOGIN_CODE_VERIFICATION_NUMBER2).send_keys(2)
        self.browser.find_element(*LoginPageLocators.LOGIN_CODE_VERIFICATION_NUMBER3).send_keys(3)
        self.browser.find_element(*LoginPageLocators.LOGIN_CODE_VERIFICATION_NUMBER4).send_keys(4)
