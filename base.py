import time
import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


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

    @allure.step('поиск элемента')
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f"Cant find element by locator {locator}")

    @allure.step('поиск элементов')
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Cant find elements by locator {locator}")

    @allure.step('переход по ссылке')
    def go_to_site(self, url=''):
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
    def sleep(self, seconds=1):
        time.sleep(seconds)

    @allure.step('переключение на другое окно')
    def switch_to_new_window(self):
        self.sleep(1)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    @allure.step('возвращение на первое окно')
    def switch_to_first_window(self):
        windows = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(windows[0])
