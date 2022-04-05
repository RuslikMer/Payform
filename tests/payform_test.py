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
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-setuid-sandbox")
        #chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-dev-shm-using")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("disable-infobars")
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
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

    def test_fill_payform(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')

    def test_fill_payform_sms_invoice(self):
        payform.go_to_site()
        payform.sign_in()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.fill_product_data('1')
        payform.send_invoice('sms')

    def test_fill_payform_link_invoice(self):
        payform.go_to_site()
        payform.sign_in()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.fill_product_data('1')
        payform.send_invoice('ссылку')

    def test_fill_payform_qr_invoice(self):
        payform.go_to_site()
        payform.sign_in()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.fill_product_data('1')
        payform.send_invoice('QR')

    def test_fill_payform_subscription(self):
        payform.go_to_site()
        payform.sign_in()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.choose_subscription()

    def test_fill_payform_course(self):
        payform.go_to_site()
        payform.sign_in()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.choose_course()

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

    def test_payments_filter_date(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.fill_date('01.01.2018', '31.03.2022', True)

    def test_payments_filter_id(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.fill_text('2993675', True)

    def test_payments_filter_phone(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.fill_text('79910002226', True)

    def test_payments_filter_method(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.select_payment_type('', True)

    def test_payments_filter_status(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.select_status('', True)

    def test_incoming_filter(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        incoming.fill_incoming_date('01.01.2018', '31.03.2022')
        payments.fill_date('01.01.2018', '31.03.2022', True)

    def test_incoming_filter_id(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.fill_text('2993675', True)

    def test_incoming_filter_phone(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.fill_text('79910002226', True)

    def test_incoming_filter_email(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.fill_text('mordasov.k@gmail.com', True)

    def test_incoming_filter_method(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.select_payment_type('', True)

    def test_incoming_filter_status(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.select_status('', True)

    def test_subscribes_filter_date(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Подписчики')
        payments.open_filters()
        subscribes.fill_last_date('01.01.2018', '31.03.2022')
        subscribes.fill_completion_date('01.01.2018', '31.03.2022')
        subscribes.fill_next_date('01.01.2018', '31.03.2022')
        subscribes.apply_filters()

    def test_subscribes_filter_phone(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Подписчики')
        payments.open_filters()
        payments.fill_text('79200271734', True)

    def test_subscribes_filter_subscription(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Подписчики')
        payments.open_filters()
        subscribes.select_subscription('', True)

    def test_subscribes_filter_state(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Подписчики')
        payments.open_filters()
        subscribes.select_state('', True)

    def test_reports_filter(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Отчёты агента')
        report.select_month('Март')
        report.generate_report()

    #def test_complaints(self):
    #    payform.go_to_site()
    #    payform.sign_in()
    #    home.go_to_page_from_footer('Жалоба')
    #    complaint.send_complaint('Тестовый Пользователь', '9991112233')

    def tearDown(self):
        print()
     #   driver.close()
     #   driver.quit()
