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

    @allure.step('проверка формы оплаты ЮMoney')
    def umoney_pay(self, order):
        self.click_to((By.XPATH, '//button[contains(.,"Оплатить")]'))
        self.wait_for_element((By.XPATH, '//div[@class="cart_wrap"][contains(.,"'+order+'")]'))

    @allure.step('скачать документы оплаты ИП')
    def download_document(self):
        self.click_to((By.XPATH, '//button[contains(.,"Скачать документы")]'))
        self.send_keys((By.NAME, 'name'), 'ООО "test"')
        self.send_keys((By.NAME, 'inn'), '3077473291')
        self.click_to((By.NAME, 'download_invoice'))
