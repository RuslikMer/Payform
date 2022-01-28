import pytest
from pages.payform import Payform


class TestSuit:
    @pytest.fixture(scope="module", autouse=True)
    def setup(self, driver):
        global payform
        payform = Payform(driver)
        payform.go_to_site()

    def test_fill_payform(self):
        payform.page_has_loaded()
        payform.set_order_number('тест')
        payform.set_phone('9991112233')
        payform.set_amount('100')
        payform.press_buy()

    def test_fill_payform_v(self):
        payform.page_has_loaded()
        payform.set_order_number('тест')
        payform.set_phone('9991112233')
        payform.set_amount('100')
        payform.press_buy()
