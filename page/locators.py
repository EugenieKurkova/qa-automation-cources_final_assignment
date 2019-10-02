from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_BOOK_ADDED = (By.CSS_SELECTOR, "#messages div:nth-child(1) > div >strong")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) > div >p>strong")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main>p")
