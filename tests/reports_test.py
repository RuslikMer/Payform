import pytest
from pages.home import Home
from pages.payform import Payform
from pages.report import Report


class TestReports:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, driver):
        global payform
        global home
        global report
        payform = Payform(driver)
        home = Home(driver)
        report = Report(driver)
        payform.go_to_site()
        payform.sign_in()

    def test_reports_filter(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Отчёты агента')
        report.select_month('Март')
        report.generate_report()
