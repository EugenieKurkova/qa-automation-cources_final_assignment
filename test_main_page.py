from .page.main_page import MainPage
from .page.login_page import LoginPage


def test_guest_should_see_login_link(parametrized_browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(parametrized_browser, url=link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(parametrized_browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(parametrized_browser, url=link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(parametrized_browser, parametrized_browser.current_url)
    login_page.should_be_login_page()
