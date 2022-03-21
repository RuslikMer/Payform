import allure
from base import BasePage
from selenium.webdriver.common.by import By


class Subscribes(BasePage):
    @allure.step('заполнение следующей даты списания')
    def fill_next_data(self, first_data, second_data):
        self.send_keys((By.NAME, 'filter_date_next_payment_start'), first_data)
        self.send_keys((By.NAME, 'filter_date_next_payment_end'), second_data)

    @allure.step('заполнение даты завершения')
    def fill_completion_data(self, first_data, second_data):
        self.send_keys((By.NAME, 'filter_date_completion_start'), first_data)
        self.send_keys((By.NAME, 'filter_date_completion_end'), second_data)

    @allure.step('заполнение последней даты списания')
    def fill_last_data(self, first_data, second_data):
        self.send_keys((By.NAME, 'filter_date_last_payment_start'), first_data)
        self.send_keys((By.NAME, 'filter_date_last_payment_end'), second_data)
