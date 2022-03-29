import sys
import time
import allure
import pytest
from datetime import datetime
from selenium import webdriver
from allure_commons.types import AttachmentType

from pages.payform import Payform
from pages.payment_systems import PaymentSystems

sys.path.append('pages')
sys.dont_write_bytecode = True


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='https://testingqa.payform.ru/',
                     help='specify the base URL to test against')
    parser.addoption('--driver', action='store', default='chrome', help='chrome or firefox')


@pytest.fixture(scope="session")
def driver(request):
    driver = request.config.getoption('--driver')
    if driver == 'firefox' or driver == 'ff':
        driver = webdriver.Firefox()
    elif driver == 'chrome':
        # chromeOptions = webdriver.ChromeOptions()
        # chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # chromeOptions.add_argument("--no-sandbox")
        # chromeOptions.add_argument("--disable-setuid-sandbox")
        # chromeOptions.add_argument("--remote-debugging-port=9222")
        # chromeOptions.add_argument("--disable-dev-shm-using")
        # chromeOptions.add_argument("--disable-extensions")
        # chromeOptions.add_argument("--disable-gpu")
        # chromeOptions.add_argument("--headless")
        # chromeOptions.add_argument("start-maximized")
        # chromeOptions.add_argument("disable-infobars")
        # driver = webdriver.Chrome(options=chromeOptions)
        driver = webdriver.Chrome()
    else:
        raise ValueError('invalid driver name: ' + driver)

    driver.set_window_size(1920, 1080)
    driver.base_url = request.config.getoption('--url') or 'https://testingqa.payform.ru/'
    yield driver
    driver.close()
    driver.quit()


# настройка хука, чтобы проверить, прошел ли тест
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


# проверка прошел ли тест
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    if request.node.rep_setup.failed:
        print("настройка теста не удалась!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['driver']
            take_screenshot(driver, request.node.nodeid)
            print("не удалось выполнить тест", request.node.nodeid)


# скриншот с названием теста, датой и временем
def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    allure.attach(driver.save_screenshot("./allure-results/" + file_name), name="Screenshot",
                  attachment_type=AttachmentType.PNG)
