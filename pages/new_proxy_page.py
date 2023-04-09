from .base_page import BasePage
from .locators import NewProxyPageLocatoros

class NewProxyPage(BasePage):
    def test_new_proxy_page_elements(self):
        title_text_proxy_page = self.browser.find_element(*NewProxyPageLocatoros.TITLE_NEW_PROXY_PAGE).text
        assert title_text_proxy_page == 'Новое доверенное лицо', f'Заголовок страницы должен быть: "Новое доверенное лицо", а не {title_text_proxy_page}'
