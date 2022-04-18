import allure
import random
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
    def fill_date(self, first_data, second_data, apply=False):
        self.send_keys((By.NAME, 'filter_date_start'), first_data)
        self.send_keys((By.NAME, 'filter_date_end'), second_data)
        if apply:
            self.apply_filters()

    @allure.step('заполнение текста')
    def fill_text(self, text, apply=False):
        self.send_keys((By.NAME, 'filter_text'), text)
        if apply:
            self.apply_filters()
        self.wait_for_element((By.XPATH, '//td[contains(.,"'+text+'")]'))

    @allure.step('выбор способа оплаты')
    def select_payment_type(self, payment_type='', apply=False):
        if payment_type == '':
            #elements = self.find_elements((By.XPATH, '//select[@name="filter_payment_type"]/following-sibling::div//li[not(@class="sel selected")]'))
            elements = self.find_elements((By.XPATH, '//td[@data-th="Способ оплаты"]/img'))
            payment_type = random.choice(elements).get_attribute('title')
        self.click_to((By.XPATH, '//select[@name="filter_payment_type"]/following-sibling::div[@class="jq-selectbox__select"]'))
        self.click_to((By.XPATH, '//li[contains(.,"' + payment_type + '")]'))
        if apply:
            self.apply_filters()
        self.wait_for_element((By.XPATH, '//td[contains(.,"' + payment_type + '")]'))

    @allure.step('выбор статуса')
    def select_status(self, status='', apply=False):
        self.click_to((By.XPATH, '//select[@name="filter_payment_status"]/following-sibling::div[@class="jq-selectbox__select"]'))
        if status == '':
            #elements = self.find_elements((By.XPATH, '//select[@name="filter_payment_status"]/following-sibling::div//li[not(@class="sel selected")]'))
            elements = self.find_elements((By.XPATH, '//td[@data-th="Статус"]'))
            status = random.choice(elements).text
        self.click_to((By.XPATH, '//li[contains(.,"' + status + '")]'))
        if apply:
            self.apply_filters()
        self.wait_for_element((By.XPATH, '//td[contains(.,"' + status + '")]'))

    @allure.step('очистка фильтра')
    def clear_filter(self):
        self.click_to((By.NAME, 'filter_payment_status'))
        self.click_to((By.XPATH, '//li[.="Очистить фильтр"]'))
