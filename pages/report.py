import os
import allure
from base import BasePage
from selenium.webdriver.common.by import By


class Report(BasePage):
    @allure.step('выбрать месяц')
    def select_month(self, month):
        self.click_to((By.XPATH, '//span[.="' + month + '"]'))

    @allure.step('сформировать отчет')
    def generate_report(self):
        self.click_to((By.NAME, 'pdf'))
