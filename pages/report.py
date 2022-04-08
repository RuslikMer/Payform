import allure
import random
from base import BasePage
from selenium.webdriver.common.by import By


class Report(BasePage):
    @allure.step('выбрать месяц')
    def select_month(self, month=''):
        if month == '':
            elements = self.find_elements((By.XPATH, '//div[@class="report-months"]//span[not(contains(@class, "disabled"))]'))
            month = random.choice(elements).text
        self.click_to((By.XPATH, '//a[contains(.,"' + month + '")]'))

    @allure.step('сформировать отчет')
    def generate_report(self):
        self.click_to((By.NAME, 'pdf'))
