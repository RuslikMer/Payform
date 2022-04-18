import os
import allure
from base import BasePage
from selenium.webdriver.common.by import By


class Home(BasePage):
    @allure.step('переход на страницу из футера')
    def go_to_page_from_footer(self, page):
        self.sleep()
        self.click_to((By.XPATH, '//a[.="'+page+'"]'))
