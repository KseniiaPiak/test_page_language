import time
from selenium.webdriver.common.by import By


def test_catalogue_language(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(10)
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(add_to_basket_button) == 1, 'Too many buttons or button not found'


