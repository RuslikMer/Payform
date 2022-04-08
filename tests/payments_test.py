import unittest
from pages.payform import Payform
from pages.payment_systems import PaymentSystems
from pages.payments import Payments
from tests.helper import webapp


class TestPayments(unittest.TestCase):
    def setUp(self):
        global payform
        global payments
        global pay_systems
        global driver
        driver = webapp.browser()
        payform = Payform(driver)
        pay_systems = PaymentSystems(driver)
        payments = Payments(driver)

    def tearDown(self):
        driver.close()
        driver.quit()

    def test_sbp(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('Быстрый платёж')
        pay_systems.sbp_pay('100')

    def test_moneta(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('Быстрый платёж')
        pay_systems.moneta_pay('100')

    def test_qiwi(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('Qiwi')
        pay_systems.qiwi_pay('100')

    def test_qiwi_rub(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('QIWI Кошелек (RUB)')
        pay_systems.qiwi_pay_rub('100')

    def test_sber(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('Сбербанк Онлайн')
        pay_systems.press_Sber_buy()

    def test_umoney(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('ЮMoney')
        pay_systems.umoney_pay('100')

    def test_ip(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('ИП')
        pay_systems.download_document()
