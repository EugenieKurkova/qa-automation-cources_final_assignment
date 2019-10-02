from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_to_basket(self):
		add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		add_to_basket_button.click()

	def should_be_added_to_basket(self):
		assert self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_ADDED).text == \
			   self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text, "Wrong book in the basket"
		assert self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_PRICE).text == \
			   self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text, "Wrong price in the basket"
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
	def should_disappear_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
