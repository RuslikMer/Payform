import allure
from base import BasePage
from selenium.webdriver.common.by import By


class Payform(BasePage):
    @allure.step('ввод номера заказа')
    def set_order_number(self):
        elem = self.find_element((By.NAME, 'order_id'))
        elem.send_keys('тест-1')

    @allure.step('ввод номера телефона')
    def set_phone(self):
        elem = self.find_element((By.NAME, 'customer_phone'))
        elem.send_keys('9991231212')

    @allure.step('задать сумму заказа')
    def set_amount(self):
        elem = self.find_element((By.NAME, 'order_sum'))
        elem.send_keys('100')

    @allure.step('нажать оплатить')
    def press_buy(self):
        elem = self.find_element((By.NAME, 'do'))
        elem.click()
