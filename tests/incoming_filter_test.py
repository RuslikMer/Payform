import unittest
from pages.home import Home
from pages.incoming import Incoming
from pages.payform import Payform
from pages.payments import Payments
from tests.helper import webapp


class TestIncomingFilter(unittest.TestCase):
    def setUp(self):
        global payform
        global payments
        global home
        global incoming
        global driver
        driver = webapp.browser()
        payform = Payform(driver)
        payments = Payments(driver)
        home = Home(driver)
        incoming = Incoming(driver)
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Возвраты')

    def tearDown(self):
        driver.close()
        driver.quit()

    def test_incoming_filter(self):
        payments.open_filters()
        incoming.fill_incoming_date('01.01.2018', '31.03.2022')
        payments.fill_date('01.01.2018', '31.03.2022', True)

    def test_incoming_filter_id(self):
        payments.open_filters()
        payments.fill_text('2700213', True)

    def test_incoming_filter_phone(self):
        payments.open_filters()
        payments.fill_text('79910002226', True)

    def test_incoming_filter_email(self):
        payments.open_filters()
        payments.fill_text('mordasov.k@gmail.com', True)

    def test_incoming_filter_method(self):
        payments.open_filters()
        payments.select_payment_type('', True)

    def test_incoming_filter_status(self):
        payments.open_filters()
        payments.select_status('', True)
