import unittest
import pytest
from pages.complaint import Complaint
from pages.home import Home
from pages.payform import Payform
from tests.helper import webapp


class TestComplaint(unittest.TestCase):
    def setUp(self):
        global payform
        global home
        global complaint
        global driver
        driver = webapp.browser()
        payform = Payform(driver)
        complaint = Complaint(driver)
        home = Home(driver)
        payform.go_to_site()
        payform.sign_in()

    def tearDown(self):
        driver.close()

    @pytest.mark.skip()
    def test_complaints(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Жалоба')
        complaint.send_complaint('Тестовый Пользователь', '9991112233')
