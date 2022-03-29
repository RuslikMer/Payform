import pytest
from pages.payform import Payform
from pages.payment_systems import PaymentSystems


@pytest.fixture
def setup(driver):
    global payform
    global pay_systems
    payform = Payform(driver)
    pay_systems = PaymentSystems(driver)


@pytest.mark.usefixtures('setup')
def test_IP():
    payform.go_to_site()
    payform.fill_payform('тест', '9991112233', '100')
    payform.press_buy('100')
    payform.choose_payment_type('ИП')
    pay_systems.download_document()
