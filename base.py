import time
import random
import string
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
#from dotenv import load_dotenv

#load_dotenv()


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
        self.actions = ActionChains(driver)

    def click_to(self, locator):
        #element = self.find_element(locator)
        #self.actions.move_to_element(element)
        #self.actions.perform()
        return self.find_element(locator).click()

    def send_keys(self, locator, text):
        self.sleep()
        #self.click_to(locator)
        #self.find_element(locator).clear()
        return self.find_element(locator).send_keys(text)

    def get_number_of_elements(self, locator):
        try:
            elements = len(self.driver.find_elements(locator))
        except Exception:
            elements = 0
        return elements

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Cant find elements by locator {locator}")

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f"Cant find element by locator {locator}")

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator),
                               message=f"Cant find element by locator {locator}")

    def get_number_from_element(self, locator):
        element = self.driver.find_element(locator)
        print(element)
        return self.driver.find_element(locator)

    def go_to_site(self, url=''):
        self.go_to(url)
        self.page_has_loaded()

    def go_to(self, url):
        url = self.base_url + url
        return self.driver.get(url)

    def page_has_loaded(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def element_exits(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def sleep(self, seconds=timeout.get('s')):
        time.sleep(seconds)

    def switch_to_new_window(self):
        self.sleep()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def switch_to_first_window(self):
        windows = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(windows[0])

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    def switch_to_iframe(self, iframe):
        self.driver.switch_to.frame(iframe)

    def switch_out_iframe(self):
        self.driver.switch_to.default_content()

    def check_js_errors(self, ignore_list=None):
        ignore_list = ignore_list or []

        logs = self.driver.get_log('browser')
        for log_message in logs:
            if log_message['level'] != 'WARNING':
                ignore = False
                for issue in ignore_list:
                    if issue in log_message['message']:
                        ignore = True
                        break

                assert ignore, 'JS error "{0}" on the page!'.format(log_message)

    def wait_page_loaded(self, timeout=60, check_js_complete=True,
                         check_page_changes=False, check_images=False,
                         wait_for_element=None,
                         wait_for_xpath_to_disappear='',
                         sleep_time=2):

        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        # Get source code of the page to track changes in HTML:
        source = ''
        try:
            source = self.driver.page_source
        except:
            pass

        # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                # Scroll down and wait when page will be loaded:
                try:
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self.driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                # Check if the page source was changed
                new_source = ''
                try:
                    new_source = self.driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            # Wait when some element will disappear:
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = self.find_element(wait_for_xpath_to_disappear)
                except:
                    pass  # Ignore timeout errors

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self.driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass  # Ignore timeout errors

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Check two times that page completely loaded:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        # Go up:
        self.driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
