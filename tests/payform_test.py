import pytest
from pages.payform import Payform


class TestSuits():
    @pytest.fixture(scope="module", autouse=True)
    def setup(self, driver):
        global payform
        payform = Payform(driver)

    @pytest.mark.usefixtures("setup")
    def test_fill_payform(self, payform):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy()

    def test_fill_payform_v(self):
        payform.go_to_site()
        payform.sign_in()

    def test_fill_payform_d(self):
        payform.go_to_site()
        payform.fill_payform('тест', '9991112233', '100')
        payform.press_buy()

    def test_fill_payform_f(self):
        payform.go_to_site()
        payform.sign_in()
