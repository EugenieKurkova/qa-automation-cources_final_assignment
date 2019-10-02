
from .page.product_page import ProductPage



def test_guest_can_add_product_to_basket(parametrized_browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(parametrized_browser, url=link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.should_be_added_to_basket()




