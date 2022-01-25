import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
