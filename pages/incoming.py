import allure
from base import BasePage
from selenium.webdriver.common.by import By


class Incoming(BasePage):
    @allure.step('заполнение даты возврата')
    def fill_incoming_date(self, first_data, second_data):
        self.send_keys((By.NAME, 'filter_incoming_date_start'), first_data)
        self.send_keys((By.NAME, 'filter_incoming_date_end'), second_data)
