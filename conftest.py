import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    # driver = request.config.getoption('--driver')
    # if driver == 'firefox' or driver == 'ff':
    #    driver = webdriver.Firefox()
    # elif driver == 'chrome':
    #    driver = webdriver.Chrome()
    # else:
    #    raise ValueError('invalid driver name: ' + driver)
    # driver.base_url = request.config.getoption('--url') or 'https://testingqa.payform.ru/'

    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.set_window_size(1920, 1080)
    driver.base_url = 'https://testingqa.payform.ru/'
    yield driver
    driver.quit()
