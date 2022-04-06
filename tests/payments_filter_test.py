import pytest
from pages.home import Home
from pages.payform import Payform
from pages.payments import Payments


class TestPaymentsFilter:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, driver):
        global payform
        global payments
        global home
        payform = Payform(driver)
        payments = Payments(driver)
        home = Home(driver)
        payform.go_to_site()
        payform.sign_in()

    def test_payments_filter_date(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.fill_date('01.01.2018', '31.03.2022', True)

    def test_payments_filter_id(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Список платежей')
        payments.open_filters()
        payments.fill_text('2993675', True)

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
