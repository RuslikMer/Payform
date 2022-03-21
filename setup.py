import pytest
from pages.payform import Payform


@pytest.fixture
def setup(self, driver):
    global payform
    payform = Payform(driver)
