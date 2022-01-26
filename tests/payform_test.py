import pytest
from pages.payform import Payform


@pytest.fixture(scope="module", autouse=True)
def setup(driver):
    global payform
    payform = Payform(driver)
    payform.go_to_site()


def test_fill_payform():
    payform.page_has_loaded()
    payform.set_order_number('тест')
    payform.set_phone('9991112233')
    payform.set_amount('100')
    payform.press_buy()

def test_fill_payform_v():
    payform.page_has_loaded()
    payform.set_order_number('тест')
    payform.set_phone('9991112233')
    payform.set_amount('100')
    payform.press_buy()
