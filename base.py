from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.actions = ActionChains(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.base_url = "https://testingqa.payform.ru/"

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator), message=f"Cant find element by locator {locator}")

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator), message=f"Cant find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'
