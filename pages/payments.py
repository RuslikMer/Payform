import allure
from base import BasePage
from selenium.webdriver.common.by import By


class Payments(BasePage):
    @allure.step('открыть фильтры')
    def open_filters(self):
        self.click_to((By.CLASS_NAME, 'switchery'))

    @allure.step('применить фильтры')
    def apply_filters(self):
        self.click_to((By.NAME, 'filter'))

    @allure.step('заполнение даты')
    def fill_data(self, first_data, second_data):
        self.send_keys((By.NAME, 'filter_date_start'), first_data)
        self.send_keys((By.NAME, 'filter_date_end'), second_data)

    @allure.step('заполнение текста')
    def fill_text(self, text):
        self.send_keys((By.NAME, 'filter_text'), text)

    @allure.step('выбор способа оплаты')
    def select_payment_type(self, payment_type):
        self.click_to((By.NAME, 'filter_payment_type'))
        self.click_to((By.XPATH, '//li[contains(.,"' + payment_type + '")]'))

    @allure.step('выбор статуса')
    def select_status(self, status):
        self.click_to((By.NAME, 'filter_payment_status'))
        self.click_to((By.XPATH, '//li[contains(.,"' + status + '")]'))

    @allure.step('очистка фильтра')
    def select_status(self):
        self.click_to((By.NAME, 'filter_payment_status'))
        self.click_to((By.XPATH, '//li[.="Очистить фильтр"]'))
