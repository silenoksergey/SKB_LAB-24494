import time

from .pages.locators import LoginPageLocators, MainPageLocators, NewProxyPageLocatoros

from .pages.login_page import LoginPage,BasePage
from .pages.new_proxy_page import NewProxyPage

import pytest

class TestAddingProxyWithoutSigningAuthority():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = LoginPageLocators.LOGIN_PAGE_LINK
        page = LoginPage(browser, url)
        page.authorization(url, login=105048, password=1234)
    def test_can_switch_to_users(self, browser):
        url = MainPageLocators.MAIN_PAGE_LINK
        page = BasePage(browser, url)
        page.go_to_stewards()
        url = NewProxyPageLocatoros.NEW_PROXY_PAGE_LINK
        page = NewProxyPage(browser, url)
        page.test_page_title()
        page.test_personal_data_block_name()
        page.test_personal_last_name_field_name()
        page.test_personal_name_field_name()
        page.test_personal_middle_name_field_name()
        page.test_personal_gender_name()
        page.test_personal_last_name_field_validation_empty_value()
        page.test_personal_name_field_validation_empty_value()






