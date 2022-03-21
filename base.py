import os
import time
import allure
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from dotenv import load_dotenv

load_dotenv()


class BasePage:
    timeout = {
        's': 1,
        'm': 3,
        'l': 6,
        'xl': 12
    }

    def __init__(self, driver):
        self.actions = ActionChains(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.base_url = driver.base_url

    @allure.step('клик по элементу')
    def click_to(self, locator):
        return self.find_element(locator).click()

    @allure.step('ввод данных')
    def send_keys(self, locator, text):
        return self.find_element(locator).send_keys(text)

    @allure.step('получить количество элементов')
    def get_number_of_elements(self, locator):
        return len(self.find_elements(locator))

    @allure.step('поиск элементов')
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Cant find elements by locator {locator}")

    @allure.step('поиск элемента')
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f"Cant find element by locator {locator}")

    @allure.step('переход по ссылке')
    def go_to_site(self, url=''):
        self.go_to(url)
        self.page_has_loaded()

    def go_to(self, url):
        url = self.base_url + url
        return self.driver.get(url)

    @allure.step('проверка что страница загрузилась')
    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    @allure.step('проверка наличия элемента')
    def element_exits(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('принудительное ожидание')
    def sleep(self, seconds=timeout.get('s')):
        time.sleep(seconds)

    @allure.step('переключение на другое окно')
    def switch_to_new_window(self):
        self.sleep()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    @allure.step('возвращение на первое окно')
    def switch_to_first_window(self):
        windows = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(windows[0])
