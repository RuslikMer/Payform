import pytest
from pages.payform import Payform
from pages.payment_systems import PaymentSystems
from pages.payments import Payments


class TestPayments:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, driver):
        global payform
        global payments
        global pay_systems
        payform = Payform(driver)
        pay_systems = PaymentSystems(driver)
        payments = Payments(driver)

    def test_qiwi(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('Qiwi')
        pay_systems.qiwi_pay('100')

    def test_sber(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('Сбербанк Онлайн')
        pay_systems.press_Sber_buy()

    def test_umoney(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        order = payform.press_buy('100')
        payform.choose_payment_type('ЮMoney')
        pay_systems.umoney_pay(order)

    def test_ip(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy('100')
        payform.choose_payment_type('ИП')
        pay_systems.download_document()
