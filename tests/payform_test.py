import unittest
import pytest
from helper import webapp
from pages.payform import Payform


class TestPayForm(unittest.TestCase):
    def setUp(self):
        global payform
        global driver
        driver = webapp.browser()
        payform = Payform(driver)
        payform.go_to_site()
        payform.sign_in()

    def tearDown(self):
        driver.close()
        driver.quit()

    def test_fill_payform_sms_invoice(self):
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.fill_product_data('1')
        payform.send_invoice('sms')

    def test_fill_payform_link_invoice(self):
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.fill_product_data('1')
        payform.send_invoice('ссылку')

    def test_fill_payform_qr_invoice(self):
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.fill_product_data('1')
        payform.send_invoice('QR')

    def test_fill_payform_subscription(self):
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.choose_subscription()

    @pytest.mark.skip()
    def test_fill_payform_course(self):
        payform.fill_payform_auth('тест', '9991112233', '100')
        payform.choose_course()
