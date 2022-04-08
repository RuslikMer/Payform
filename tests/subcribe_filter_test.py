import unittest
from pages.home import Home
from pages.payform import Payform
from pages.payment_systems import PaymentSystems
from pages.payments import Payments
from pages.subscribes import Subscribes
from tests.helper import webapp


class TestSubscribesFilter(unittest.TestCase):
    def setUp(self):
        global payform
        global payments
        global pay_systems
        global home
        global subscribes
        global driver
        driver = webapp.browser()
        payform = Payform(driver)
        pay_systems = PaymentSystems(driver)
        payments = Payments(driver)
        home = Home(driver)
        subscribes = Subscribes(driver)
        payform.go_to_site()
        payform.sign_in()

    def tearDown(self):
        driver.close()
        driver.quit()

    def test_subscribes_filter_date(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Подписчики')
        payments.open_filters()
        subscribes.fill_last_date('01.01.2018', '31.03.2022')
        subscribes.fill_completion_date('01.01.2018', '31.03.2022')
        subscribes.fill_next_date('01.01.2018', '31.03.2022')
        subscribes.apply_filters()

    def test_subscribes_filter_phone(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Подписчики')
        payments.open_filters()
        payments.fill_text('79200271734', True)

    def test_subscribes_filter_subscription(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Подписчики')
        payments.open_filters()
        subscribes.select_subscription('', True)

    def test_subscribes_filter_state(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Подписчики')
        payments.open_filters()
        subscribes.select_state('', True)
