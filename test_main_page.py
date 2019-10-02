import pytest
from .page.base_page import BasePage
from .page.login_page import LoginPage
from .page.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, parametrized_browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = BasePage(parametrized_browser, url=link)
        page.open()
        page.should_be_login_link()


    def test_guest_can_go_to_login_page(self, parametrized_browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = BasePage(parametrized_browser, url=link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(parametrized_browser, parametrized_browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(parametrized_browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(parametrized_browser, url=link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(parametrized_browser, parametrized_browser.current_url)
    basket_page.should_there_be_no_books_in_the_basket()

def test_guest_can_see_empty_basket_opened_from_main_page(parametrized_browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(parametrized_browser, url=link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(parametrized_browser, parametrized_browser.current_url)
    basket_page.should_the_basket_be_empty()
