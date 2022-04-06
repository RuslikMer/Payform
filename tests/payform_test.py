import pytest
from pages.payform import Payform


class TestPayForm:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, driver):
        global payform
        payform = Payform(driver)
        payform.go_to_site()
        payform.sign_in()

    def test_fill_payform_sms_invoice(self):
        payform.go_to_site()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.fill_product_data('1')
        payform.send_invoice('sms')

    def test_fill_payform_link_invoice(self):
        payform.go_to_site()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.fill_product_data('1')
        payform.send_invoice('ссылку')

    def test_fill_payform_qr_invoice(self):
        payform.go_to_site()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.fill_product_data('1')
        payform.send_invoice('QR')

    def test_fill_payform_subscription(self):
        payform.go_to_site()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.choose_subscription()

    def test_fill_payform_course(self):
        payform.go_to_site()
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.choose_course()
