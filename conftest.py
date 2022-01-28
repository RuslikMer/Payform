import sys
import pytest
from selenium import webdriver


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
