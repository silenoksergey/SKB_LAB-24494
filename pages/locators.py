from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_PAGE_LINK = 'https://delo-prod.skblab.ru/login'
    LOGIN_FIELD = (By.CSS_SELECTOR, 'input.with-icon.text')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '.with-icon.password.ng-untouched.ng-pristine.ng-valid')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.button.button-login.legacy > button')
    LOGIN_CODE_VERIFICATION_NUMBER1 = (By.CSS_SELECTOR, 'form.sms-container.ng-pristine > div:nth-child(1) > input')
    LOGIN_CODE_VERIFICATION_NUMBER2 = (By.CSS_SELECTOR, 'form.sms-container.ng-pristine > div:nth-child(2) > input')
    LOGIN_CODE_VERIFICATION_NUMBER3 = (By.CSS_SELECTOR, 'form.sms-container.ng-pristine > div:nth-child(3) > input')
    LOGIN_CODE_VERIFICATION_NUMBER4 = (By.CSS_SELECTOR, 'form.sms-container.ng-pristine > div:nth-child(4) > input')
class MainPageLocators():
    MAIN_PAGE_LINK = 'https://delo-prod.skblab.ru/summary'
    PROFILE_BUTTON = (By.CSS_SELECTOR, '.next-icon-settings')

class ProfilePageLocators():
    TAB_USERS = (By.CSS_SELECTOR, '[selenium-id=profile-users-tab]')
    ADD_USER_BUTTON = (By.CSS_SELECTOR, '#relation-add-button')
class NewProxyPageLocatoros():
    TITLE_NEW_PROXY_PAGE = (By.CSS_SELECTOR, 'div.section-body > div.section-title')
    NEW_PROXY_PAGE_LINK = 'https://delo-prod.skblab.ru/depositee/create'