import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_presence(browser):
    browser.get(link)
    time.sleep(3)  # Для демонстрации, обычно лучше использовать явные ожидания
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR,".btn-add-to-basket")
    assert add_to_cart_button is not None, "Add to cart button is not found on the page!"
