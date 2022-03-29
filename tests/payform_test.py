import pytest
from pages.payform import Payform


@pytest.fixture
def setup(driver):
    global payform
    payform = Payform(driver)


@pytest.mark.usefixtures('setup')
def test_fill_payform():
    payform.go_to_site()
    payform.fill_payform('тест', '9991112233', '100')


@pytest.mark.usefixtures('setup')
def test_fill_payform_auth():
    payform.go_to_site()
    payform.sign_in()
    payform.fill_payform('тест', '9991112233')
    payform.fill_product_data('100', '1')
