import unittest
from pages.home import Home
from pages.payform import Payform
from pages.report import Report
from tests.helper import webapp


class TestReports(unittest.TestCase):
    def setUp(self):
        global payform
        global home
        global report
        global driver
        driver = webapp.browser()
        payform = Payform(driver)
        home = Home(driver)
        report = Report(driver)
        payform.go_to_site()
        payform.sign_in()

    def tearDown(self):
        driver.close()
        driver.quit()

    def test_reports_filter(self):
        payform.go_to_site()
        home.go_to_page_from_footer('Отчёты агента')
        report.select_month()
        report.generate_report()
