import sys
import time
from datetime import datetime
import allure
import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType

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
        driver = webdriver.Chrome()
    else:
        raise ValueError('invalid driver name: ' + driver)

    # driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.set_window_size(1920, 1080)
    driver.base_url = request.config.getoption('--url') or 'https://testingqa.payform.ru/'
    yield driver
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
            driver = request.node.funcargs['selenium_driver']
            take_screenshot(driver, request.node.nodeid)
            print("не удалось выполнить тест", request.node.nodeid)


# скриншот с названием теста, датой и временем
def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    allure.attach(driver.save_screenshot(file_name), name="Screenshot", attachment_type=AttachmentType.PNG)
