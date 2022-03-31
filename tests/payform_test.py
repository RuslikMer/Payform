import pytest
import unittest

from pages.complaint import Complaint
from pages.home import Home
from pages.incoming import Incoming
from pages.payform import Payform
from selenium import webdriver
from pages.payment_systems import PaymentSystems
from pages.payments import Payments
from pages.report import Report
from pages.subscribes import Subscribes


class TestPayform(unittest.TestCase):
    def setUp(self):
        global driver
        chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        chromeOptions.add_argument("--no-sandbox")
        chromeOptions.add_argument("--disable-setuid-sandbox")
        #chromeOptions.add_argument("--remote-debugging-port=9222")
        chromeOptions.add_argument("--disable-dev-shm-using")
        chromeOptions.add_argument("--disable-extensions")
        #chromeOptions.add_argument("--disable-gpu")
        # chromeOptions.add_argument("--headless")
        #chromeOptions.add_argument("start-maximized")
        chromeOptions.add_argument("disable-infobars")
        driver = webdriver.Chrome(options=chromeOptions)
        #driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.base_url = 'https://testingqa.payform.ru/'
        global payform
        global payments
        global pay_systems
        global home
        global incoming
        global subscribes
        global report
        global complaint
        payform = Payform(driver)
        complaint = Complaint(driver)
        pay_systems = PaymentSystems(driver)
        payments = Payments(driver)
        home = Home(driver)
        incoming = Incoming(driver)
        subscribes = Subscribes(driver)
        report = Report(driver)

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

    def test_payments_filter(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.fill_data('01.01.2018', '31.03.2022')
        payments.apply_filters()

    def test_incoming_filter(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.fill_data('01.01.2018', '31.03.2022')
        incoming.fill_incoming_data('01.01.2018', '31.03.2022')
        payments.apply_filters()

    def test_subscribes_filter(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Подписчики')
        payments.open_filters()
        subscribes.fill_last_data('01.01.2018', '31.03.2022')
        subscribes.fill_completion_data('01.01.2018', '31.03.2022')
        subscribes.fill_next_data('01.01.2018', '31.03.2022')
        subscribes.apply_filters()

    def test_reports_filter(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Отчёты агента')
        report.select_month('Март')
        report.generate_report()

    def test_complaints(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Жалоба')
        complaint.send_complaint('Тестовый Пользователь', '9991112233')

    def tearDown(self):
        driver.close()
        driver.quit()
