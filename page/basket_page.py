from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_be_basket_url(self):
	    assert "basket" in self.browser.current_url, "Basket URL is not presented"

	def should_there_be_no_books_in_the_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BOOK_IN_THE_BASKET), \
       "Books are in the basket, but should not be"

	def should_the_basket_be_empty(self):
		assert self.is_element_present(*BasketPageLocators.NO_BOOK_CONTINUE_SHOPPING), \
       "Books are in the basket, but should not be"


