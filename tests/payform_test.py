import pytest
import unittest

from pages.home import Home
from pages.payform import Payform
from selenium import webdriver
from pages.payment_systems import PaymentSystems
from pages.payments import Payments


class TestPayform(unittest.TestCase):
    def setUp(self):
        global driver
        chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-setuid-sandbox")
        chromeOptions.add_argument("--remote-debugging-port=9222")
        chromeOptions.add_argument("--disable-dev-shm-using")
        chromeOptions.add_argument("--disable-extensions")
        chromeOptions.add_argument("--disable-gpu")
        # chromeOptions.add_argument("--headless")
        chromeOptions.add_argument("start-maximized")
        chromeOptions.add_argument("disable-infobars")
        driver = webdriver.Chrome(options=chromeOptions)
        #driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.base_url = 'https://testingqa.payform.ru/'
        global payform
        global payments
        global pay_systems
        global home
        payform = Payform(driver)
        pay_systems = PaymentSystems(driver)
        payments = Payments(driver)
        home = Home(driver)

    def test_fill_payform_auth(self):
        payform.go_to_site()
        payform.sign_in()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.fill_product_data('100', '1')

    def test_fill_payform(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')

    def test_Qiwi(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('Qiwi')
        pay_systems.qiwi_pay('100')

    def test_Sber(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('Сбербанк Онлайн')
        pay_systems.press_Sber_buy()

    def test_Umoney(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        order = payform.press_buy('100')
        payform.choose_payment_type('ЮMoney')
        pay_systems.umoney_pay(order)

    def test_IP(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('ИП')
        pay_systems.download_document()

    def payments_filter(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Платежи')
        payments.open_filters()
        payments.fill_data('01.01.2018', '31.03.2022')
        payments.apply_filters()

    def tearDown(self):
        driver.close()
        driver.quit()
