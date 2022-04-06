from selenium import webdriver


def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--remote-debugging-port=9222")
    # chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-dev-shm-using")
    # chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.base_url = 'https://mordasov.payform.ru'

    return driver
