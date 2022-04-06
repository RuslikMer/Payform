import pytest
from pages.complaint import Complaint
from pages.home import Home
from pages.payform import Payform


class TestComplaint:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, driver):
        global payform
        global home
        global complaint
        payform = Payform(driver)
        complaint = Complaint(driver)
        home = Home(driver)

    def test_complaints(self):
        payform.go_to_site()
        payform.sign_in()
        home.go_to_page_from_footer('Жалоба')
        complaint.send_complaint('Тестовый Пользователь', '9991112233')
