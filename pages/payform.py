import os
import allure
from base import BasePage
from selenium.webdriver.common.by import By


class Payform(BasePage):
    @allure.step('заполнение формы для оплаты неавторизованным пользователем')
    def fill_payform(self, order, phone, price='', email='test@mail.ru', extra='тестовый заказ'):
        self.send_keys((By.NAME, 'order_id'), order)
        self.send_keys((By.NAME, 'customer_phone'), phone)
        if self.get_number_of_elements((By.NAME, 'products[cur_1][price]')) == 0:
            self.send_keys((By.NAME, 'order_sum'), price)
        self.send_keys((By.NAME, 'customer_email'), email)
        self.send_keys((By.NAME, 'customer_extra'), extra)

    @allure.step('заполнение формы для оплаты авторизованным пользователем')
    def fill_payform_auth(self, order, phone, price='', email='test@mail.ru', extra='тестовый заказ'):
        self.send_keys((By.NAME, 'order_id'), order)
        self.send_keys((By.NAME, 'customer_phone'), phone)
        self.send_keys((By.NAME, 'products[cur_1][price]'), price)
        self.wait_for_element((By.XPATH, '//span[@class="paygoods-product-sum"][contains(.,"' + price + '")]'))
        self.send_keys((By.NAME, 'customer_email'), email)
        self.send_keys((By.NAME, 'customer_extra'), extra)

    @allure.step('нажатие кнопки оплатить')
    def press_buy(self, price):
        self.sleep()
        self.click_to((By.NAME, 'do'))
        self.wait_for_element((By.XPATH, '//span[contains(@class, "price")][contains(., "'+price+'")]'))
        #return self.get_number_from_element((By.TAG_NAME, 'h1'))

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
        if self.get_number_of_elements((By.XPATH, '//span[contains(.,"'+service_type+'")]')) == 0:
            self.click_to((By.XPATH, '//label[not(contains(@class, "hidden"))]/*[contains(.,"'+service_type+'")]'))

    @allure.step('заполнение данных по товару')
    def fill_product_data(self, price, quantity, name='тест'):
        self.change_service('товары')
        self.send_keys((By.NAME, 'products[cur_1][name]'), name)
        self.send_keys((By.NAME, 'products[cur_1][quantity]'), quantity)

    @allure.step('выбор курса')
    def choose_course(self):
        self.change_service('курс')
        self.click_to((By.XPATH, '//div[contains(@class,"input-course")]//div[@class="jq-selectbox__select"]'))
        self.click_to((By.XPATH, '//div[contains(@class,"input-course")]//div[@class="jq-selectbox__dropdown"]//li[not(contains(.,"выберите курс"))]'))

    @allure.step('выбор подписки')
    def choose_subscription(self):
        self.change_service('подписк')
        self.click_to((By.XPATH, '//div[contains(@class,"input-subscription")]//div[@class="jq-selectbox__select"]'))
        self.click_to((By.XPATH, '//div[contains(@class,"input-subscription")]//div[@class="jq-selectbox__dropdown"]//li[not(contains(.,"не выбрана"))]'))

    @allure.step('отправить счёт')
    def send_invoice(self, type):
        self.click_to((By.XPATH, '//a[.="Отправить счет"]'))
        self.click_to((By.XPATH, '//button[contains(.,"'+type+'")]'))
