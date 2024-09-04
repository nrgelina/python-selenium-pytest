from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

	def should_be_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), (
			"Basket is not empty")

	def should_not_be_basket_items(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
			"Item is presented in basket, but should not be"

	def go_to_checkout(self):
		link = self.browser.find_element(*BasketPageLocators.CHECKOUT_BUTTON)
		link.click()

	def should_not_have_checkout_option(self):
		assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), \
			"Checkout button is presented, but should not be"

