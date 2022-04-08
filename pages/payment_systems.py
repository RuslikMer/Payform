import allure
from base import BasePage
from selenium.webdriver.common.by import By


class PaymentSystems(BasePage):
    @allure.step('проверка формы оплаты Sberbank')
    def press_Sber_buy(self):
        self.click_to((By.NAME, 'go'))

    @allure.step('проверка формы оплаты QIWI')
    def qiwi_pay(self, price):
        self.wait_for_element((By.XPATH, '//span[@class="price__amount"][contains(.,"'+price+'")]'))

    @allure.step('проверка формы оплаты SBP')
    def sbp_pay(self, price):
        self.click_to((By.XPATH, '//a[contains(.,"Оплатить")]'))
        self.switch_to_new_window()
        self.wait_for_element((By.XPATH, '//div[@class="info"]//p[@class="info-text"][contains(.,"' + price + '")]'))

    @allure.step('проверка формы оплаты Moneta')
    def moneta_pay(self, price):
        self.click_to((By.XPATH, '//a[contains(.,"Moneta")]'))
        self.wait_for_element((By.XPATH, '//td[@class="cart_amount_value_td"][contains(.,"' + price + '")]'))

    @allure.step('проверка формы оплаты QIWI RUB')
    def qiwi_pay_rub(self, price):
        self.wait_for_element((By.XPATH, '//div[@id="InvoiceInfoView-Amount"][contains(.,"' + price + '")]'))

    @allure.step('проверка формы оплаты ЮMoney')
    def umoney_pay(self, price):
        self.wait_for_element((By.XPATH, '//div[contains(@class, "qa-payment-info2-price")][contains(.,"'+price+'")]'))

    @allure.step('скачать документы оплаты ИП')
    def download_document(self):
        self.click_to((By.XPATH, '//button[contains(.,"Скачать документы")]'))
        self.send_keys((By.NAME, 'name'), 'ООО "test"')
        self.send_keys((By.NAME, 'inn'), '3077473291')
        self.click_to((By.NAME, 'download_invoice'))
