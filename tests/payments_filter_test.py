import unittest
from pages.home import Home
from pages.payform import Payform
from pages.payments import Payments
from tests.helper import webapp


class TestPaymentsFilter(unittest.TestCase):
    def setUp(self):
        global payform
        global payments
        global home
        global driver
        driver = webapp.browser()
        payform = Payform(driver)
        payments = Payments(driver)
        home = Home(driver)
        payform.go_to_site()
        payform.sign_in()

    def tearDown(self):
        driver.close()
        driver.quit()

    def test_payments_filter_date(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.fill_date('01.01.2018', '31.03.2022', True)

    def test_payments_filter_id(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.fill_text('3272371', True)

    def test_payments_filter_phone(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.fill_text('79910002226', True)

    def test_payments_filter_method(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.select_payment_type('', True)

    def test_payments_filter_status(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.select_status('', True)
