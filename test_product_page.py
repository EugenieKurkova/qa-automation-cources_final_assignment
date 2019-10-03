import pytest
import time
from .page.product_page import ProductPage
from .page.login_page import LoginPage
from .page.basket_page import BasketPage


link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.need_review
@pytest.mark.parametrize('link', [link,
								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(parametrized_browser, link):
	page = ProductPage(parametrized_browser, url=link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.should_be_added_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(parametrized_browser):
	page = ProductPage(parametrized_browser, url=link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.should_not_be_success_message()


def test_should_not_be_success_message(parametrized_browser):
	page = ProductPage(parametrized_browser, url=link)
	page.open()
	page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(parametrized_browser):
	page = ProductPage(parametrized_browser, url=link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(parametrized_browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(parametrized_browser, url=link)
	page.open()
	page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(parametrized_browser):
	link = "http://selenium1py.pythonanywhere.com"
	page = ProductPage(parametrized_browser, url=link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(parametrized_browser, parametrized_browser.current_url)
	login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(parametrized_browser):
	link = "http://selenium1py.pythonanywhere.com"
	page = ProductPage(parametrized_browser, url=link)
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(parametrized_browser, parametrized_browser.current_url)
	basket_page.should_there_be_no_books_in_the_basket()


def test_guest_can_see_empty_basket_opened_from_product_page(parametrized_browser):
	link = "http://selenium1py.pythonanywhere.com"
	page = ProductPage(parametrized_browser, url=link)
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(parametrized_browser, parametrized_browser.current_url)
	basket_page.should_the_basket_be_empty()


class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, parametrized_browser):
		link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
		page = LoginPage(parametrized_browser, url=link)
		page.open()
		email = str(time.time()) + "@fakemail.org"
		page.register_new_user(email, "SemQuestionar1&")
		time.sleep(3)
		page.should_be_authorized_user()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, parametrized_browser):
		page = ProductPage(parametrized_browser, url=link)
		page.open()
		page.add_to_basket()
		page.solve_quiz_and_get_code()
		page.should_be_added_to_basket()

	@pytest.mark.xfail
	def test_user_cant_see_success_message_after_adding_product_to_basket(self, parametrized_browser):
		page = ProductPage(parametrized_browser, url=link)
		page.open()
		page.add_to_basket()
		page.solve_quiz_and_get_code()
		page.should_not_be_success_message()
