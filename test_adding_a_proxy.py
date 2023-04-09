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
        page.authorization(url, login=352371, password=1234)
    def test_can_switch_to_users(self, browser):
        url = MainPageLocators.MAIN_PAGE_LINK
        page = BasePage(browser, url)
        page.go_to_stewards()
        url = NewProxyPageLocatoros.NEW_PROXY_PAGE_LINK
        page = NewProxyPage(browser, url)
        page.test_new_proxy_page_elements()











