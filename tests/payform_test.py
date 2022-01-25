from pages.payform import Payform


def test_fill_payform(browser):
    payform = Payform(browser)

    payform.go_to_site()
    payform.page_has_loaded()
    payform.set_order_number()
    payform.set_phone()
    payform.set_amount()
    payform.press_buy()
