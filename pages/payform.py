import os
import allure
from base import BasePage
from selenium.webdriver.common.by import By


class Payform(BasePage):
    @allure.step('заполнение формы для оплаты неавторизованным пользователем')
    def fill_payform(self, order, phone, amount, email='', extra=''):
        self.send_keys((By.NAME, 'order_id'), order)
        self.send_keys((By.NAME, 'customer_phone'), phone)
        self.send_keys((By.NAME, 'order_sum'), amount)
        self.send_keys((By.NAME, 'customer_email'), email)
        self.send_keys((By.NAME, 'customer_extra'), extra)

    @allure.step('нажатие кнопки оплатить')
    def press_buy(self):
        self.click_to((By.NAME, 'do'))

    @allure.step('выбор способа оплаты')
    def choose_payment_type(self, payment):
        self.click_to((By.XPATH, '//a[contains(@id,"payment-method")][not(@style)][contains(.,"'+payment+'")]'))

    @allure.step('возврат на страницу payform')
    def go_back_to_payform(self):
        self.click_to((By.XPATH, '//a[@href="/"][contains(@class,"btn")]'))

    @allure.step('очистка payform')
    def clear_payform(self):
        self.click_to((By.XPATH, '//a[@title="Очистить"]'))

    @allure.step('авторизация')
    def sign_in(self, email=os.getenv('EMAIL'), password=os.getenv('PASS')):
        self.click_to((By.XPATH, '//a[@data-prodamus-open="auth.login"]'))
        self.send_keys((By.ID, 'userMail'), email)
        self.send_keys((By.NAME, 'auth_password'), password)
        self.click_to((By.XPATH, '//span[@title="Войти"]'))

    @allure.step('изменить услугу')
    def change_service(self, service_type):
        if self.get_number_of_elements((By.NAME, '//span[.="'+service_type+'"]')):
            self.click_to((By.XPATH, '//label[not(contains(@class, "hidden"))]/a[contains(.,"'+service_type+'")]'))

    @allure.step('заполнение данных по товару')
    def fill_product_data(self, name, price, quantity):
        self.change_service('товары')
        self.send_keys((By.NAME, 'products[cur_1][name]'), name)
        self.send_keys((By.NAME, 'products[cur_1][price]'), price)
        self.send_keys((By.NAME, 'products[cur_1][quantity]'), quantity)
