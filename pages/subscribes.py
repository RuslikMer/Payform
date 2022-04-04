import random
import allure
from base import BasePage
from selenium.webdriver.common.by import By


class Subscribes(BasePage):
    @allure.step('заполнение следующей даты списания')
    def fill_next_date(self, first_data, second_data):
        self.send_keys((By.NAME, 'filter_date_next_payment_start'), first_data)
        self.send_keys((By.NAME, 'filter_date_next_payment_end'), second_data)

    @allure.step('заполнение даты завершения')
    def fill_completion_date(self, first_data, second_data):
        self.send_keys((By.NAME, 'filter_date_completion_start'), first_data)
        self.send_keys((By.NAME, 'filter_date_completion_end'), second_data)

    @allure.step('заполнение последней даты списания')
    def fill_last_date(self, first_data, second_data):
        self.send_keys((By.NAME, 'filter_date_last_payment_start'), first_data)
        self.send_keys((By.NAME, 'filter_date_last_payment_end'), second_data)

    @allure.step('применить фильтры')
    def apply_filters(self):
        self.click_to((By.XPATH, '//button[.="Применить"]'))

    @allure.step('выбор подписки')
    def select_subscription(self, subscription='', apply=False):
        self.click_to((By.XPATH, '//select[@name="filter_subscription"]/following-sibling::div[@class="jq-selectbox__select"]'))
        if subscription == '':
            elements = self.find_elements((By.XPATH, '//select[@name="filter_subscription"]/following-sibling::div//li[not(@class="sel selected")]'))
            subscription = random.choice(elements).text
        self.click_to((By.XPATH, '//li[contains(.,"' + subscription + '")]'))
        if apply:
            self.apply_filters()
        self.wait_for_element((By.XPATH, '//td[contains(.,"' + subscription + '")]'))

    @allure.step('выбор состояния')
    def select_state(self, state='', apply=False):
        self.click_to((By.XPATH, '//select[@name="filter_state"]/following-sibling::div[@class="jq-selectbox__select"]'))
        if state == '':
            elements = self.find_elements((By.XPATH, '//select[@name="filter_state"]/following-sibling::div//li[not(@class="sel selected")]'))
            state = random.choice(elements).text
        self.click_to((By.XPATH, '//li[contains(.,"' + state + '")]'))
        if apply:
            self.apply_filters()
        self.wait_for_element((By.XPATH, '//td[contains(.,"' + state + '")]'))