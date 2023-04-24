import time

from selenium.webdriver import ActionChains
import random
from .base_page import BasePage
from .locators import NewProxyPageLocatoros
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class NewProxyPage(BasePage):

    """"Проверка заголовка на странице Новое доверенное лицо"""
    def test_page_title(self):
        title_text_proxy_page = self.browser.find_element(*NewProxyPageLocatoros.TITLE_NEW_PROXY_PAGE).text
        assert title_text_proxy_page == 'Новое доверенное лицо', f'Заголовок страницы должен быть: "Новое доверенное лицо", а не {title_text_proxy_page}'

    """Проверка отображения наименования блока Личные данные"""
    def test_personal_data_block_name(self):
        personal_data_block_name = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_PERSONAL_DATA_NAME).text
        assert personal_data_block_name == 'Личные данные', f'Наименование блока должно быть: "Личные данные", а не {personal_data_block_name}'

    """Проверка отображения поля Фамилия"""
    def test_personal_last_name_field_name(self):
        field_last_name = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_FIELD_LAST_NAME).text
        assert field_last_name == 'Фамилия', f'Наименование поля должно быть: "Фамилия", а не {field_last_name}'


    """Проверка отображения поля Имя"""
    def test_personal_name_field_name(self):
        field_name = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_FIELD_NAME).text
        assert field_name == 'Имя', f'Наименование поля должно быть: "Имя", а не {field_name}'


    """Проверка отображения поля Отчество"""
    def test_personal_middle_name_field_name(self):
        field_middle_name = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_FIELD_MIDDLE_NAME).text
        assert field_middle_name == 'Отчество', f'Наименование поля должно быть: "Отчество", а не {field_middle_name}'


    """Проверка отображения валидации поля Фамилия при снятии фокуса с незаполненного поля"""
    def test_personal_last_name_field_validation_empty_value(self):
        last_name_field_input = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_FIELD_LAST_NAME_INPUT)
        last_name_field_input.click()
        last_name_field_input.send_keys(Keys.TAB)
        validation_text_last_name_field = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_VALIDATION_LAST_NAME_FIELD).text
        assert validation_text_last_name_field == "Обязательно для заполнения", f'Под полем должна отображаться валидация с текстом "Обязательно для заполнения", а не {validation_text_last_name_field}'


    """Проверка отображения валидации поля Имя при снятии фокуса с незаполненного поля"""
    def test_personal_name_field_validation_empty_value(self):
        name_field_input = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_FIELD_NAME_INPUT)
        name_field_input.click()
        name_field_input.send_keys(Keys.TAB)
        validation_text_name_field = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_VALIDATION_NAME_FIELD).text
        assert validation_text_name_field == "Обязательно для заполнения", f'Под полем должна отображаться валидация с текстом "Обязательно для заполнения", а не {validation_text_name_field}'

    # """"Проверяем, что после ввода одного символа в поле Фамилия не сработала валидация"""
    # def test_last_name_field_no_validation_at_single_characters(self):
    #     last_name_field_input = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_FIELD_LAST_NAME_INPUT)
    #     last_name_field_input.send_keys(self.cyrillic_letter_generation(1))
    #     assert self.is_not_element_present(*NewProxyPageLocatoros.NEW_PROXY_VALIDATION_LAST_NAME_FIELD), \
    #         "Сработала валидация при вводе одного символа"
    #
    #
    #
    # """"Проверяем, что после ввода пятидесяти символов в поле Фамилия не сработала валидация"""
    # def test_last_name_field_no_validation_at_fifty_characters(self):
    #     last_name_field_input = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_FIELD_LAST_NAME_INPUT)
    #     last_name_field_input.send_keys(self.cyrillic_letter_generation(50))
    #     assert self.is_not_element_present(*NewProxyPageLocatoros.NEW_PROXY_VALIDATION_LAST_NAME_FIELD), \
    #         "Сработала валидация при вводе пятидесяти символов"
    #
    #
    #
    """"Проверяем, что после ввода пятидесяти одного символа в поле Фамилия сработала валидация"""

    """"Проверяем, что после ввода одного символа в поле Имя не сработала валидация"""

    """"Проверяем, что после ввода пятидесяти символов в поле Имя не сработала валидация"""

    """"Проверяем, что после ввода пятидесяти одного символа в поле Имя сработала валидация"""

    """"Проверяем, что после ввода пятидесяти символов в поле Отчество не сработала валидация"""

    """"Проверяем, что после ввода пятидесяти одного символа в Отчество Имя сработала валидация"""

    """Проверка отображения блока Пол"""
    def test_personal_gender_name(self):
        gender_name = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_GENDER_NAME).text
        assert gender_name == 'Пол', f'Наименование поля должно быть: "Пол", а не {gender_name}'

    """Проверка отображения блока Контактная информация"""
    def test_block_contact_info(self):
        block_name_contact_info = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_BLOCK_NAME_CONTACT_INFO).text
        assert block_name_contact_info == 'Контактная информация', f'Наименование блока должно быть: "Контактная информация",а не {block_name_contact_info}'


    """Проверка отображения поля Телефон доверенного лица"""
    def test_name_field_trusted_person_phone_number(self):
        field_name_contact_info = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_FIELD_NAME_TRUSTED_PERSON_PHONE_NUMBER).text
        assert field_name_contact_info == 'Телефон доверенного лица', f'Наименование блока должно быть: "Телефон доверенного лица",а не {field_name_contact_info}'

    """Проверка подсказки у поля Телефон доверенного лица"""
    def test_checking_prompt_trusted_person_phone_number_field(self):
        prompt_trusted_person_phone_number_field = self.browser.find_element(*NewProxyPageLocatoros.NEW_PROXY_PROMPT_TRUSTED_PERSONAL_PHONE_NUMBER)
        prompt_text = prompt_trusted_person_phone_number_field.get_attribute("mattooltip")
        assert prompt_text == 'На этот номер телефона придет СМС/push с кодом подтверждения', f'Текст подсказки {prompt_text}, а не "На этот номер телефона придет СМС/push с кодом подтверждения"'