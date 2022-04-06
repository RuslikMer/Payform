import pytest
from pages.home import Home
from pages.incoming import Incoming
from pages.payform import Payform
from pages.payments import Payments


class TestIncomingFilter:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, driver):
        global payform
        global payments
        global home
        global incoming
        payform = Payform(driver)
        payments = Payments(driver)
        home = Home(driver)
        incoming = Incoming(driver)
        payform.go_to_site()
        payform.sign_in()

    def test_incoming_filter(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        incoming.fill_incoming_date('01.01.2018', '31.03.2022')
        payments.fill_date('01.01.2018', '31.03.2022', True)

    def test_incoming_filter_id(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.fill_text('2993675', True)

    def test_incoming_filter_phone(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.fill_text('79910002226', True)

    def test_incoming_filter_email(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.fill_text('mordasov.k@gmail.com', True)

    def test_incoming_filter_method(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.select_payment_type('', True)

    def test_incoming_filter_status(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Возвраты')
        payments.open_filters()
        payments.select_status('', True)
