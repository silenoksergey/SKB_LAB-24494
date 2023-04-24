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
    NEW_PROXY_PERSONAL_DATA_NAME = (By.CSS_SELECTOR, 'div.container > corporate-depositee-create > div > form > div.section-body > div:nth-child(2) > div:nth-child(1) > .block-name')
    NEW_PROXY_FIELD_LAST_NAME = (By.CSS_SELECTOR, '[formcontrolname=last_name] > mat-form-field > div > div> div > span > label > mat-label')
    NEW_PROXY_FIELD_NAME = (By.CSS_SELECTOR, '[formcontrolname=name] > mat-form-field > div > div> div > span > label')
    NEW_PROXY_FIELD_MIDDLE_NAME = (By.CSS_SELECTOR, '[formcontrolname=mdl_name] > mat-form-field > div > div> div > span > label > mat-label')
    NEW_PROXY_FIELD_LAST_NAME_INPUT = (By.CSS_SELECTOR, '[formcontrolname=last_name] > mat-form-field > div > div > .mat-form-field-infix > input')
    NEW_PROXY_FIELD_NAME_INPUT = (By.CSS_SELECTOR, '[formcontrolname=name] > mat-form-field > div > div> div > input')
    NEW_PROXY_GENDER_NAME = (By.CSS_SELECTOR, 'div.block-data > span')
    NEW_PROXY_VALIDATION_LAST_NAME_FIELD = (By.CSS_SELECTOR, 'div.block-data > ui-error:nth-child(2) > div')
    NEW_PROXY_VALIDATION_NAME_FIELD = (By.CSS_SELECTOR, 'div.block-data > ui-error:nth-child(4) > div')
