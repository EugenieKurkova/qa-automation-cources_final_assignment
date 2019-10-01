from .page.main_page import MainPage


def test_guest_can_go_to_login_page(parametrized_browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(parametrized_browser, url=link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()


def test_guest_should_see_login_link(parametrized_browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(parametrized_browser, url=link)
    page.open()
    page.should_be_login_link()