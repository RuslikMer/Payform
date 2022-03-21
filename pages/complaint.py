import allure
from base import BasePage
from selenium.webdriver.common.by import By


class Complaint(BasePage):
    @allure.step('отправка жалобы')
    def send_complaint(self, name, phone, email, text):
        self.send_keys((By.NAME, 'name'), name)
        self.send_keys((By.NAME, 'phone'), phone)
        self.send_keys((By.NAME, 'email'), email)
        self.send_keys((By.NAME, 'text'), text)
        self.click_to((By.XPATH, '//button[contains(.,"Отправить ")]'))
