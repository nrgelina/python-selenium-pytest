import time

from .base_page import BasePage
from .locators import ProductPageLocators, CheckoutPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

	def add_to_basket(self):
		basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
		basket.click()

	def should_be_message_basket_item(self):
		assert self.is_element_present(*ProductPageLocators.ITEM_NAME), (
			"Product name is not presented")
		assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_ITEM), (
			"Message about adding is not presented")

		item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
		message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_ITEM).text
		assert "{} has been added to your basket.".format(item_name) == message, \
			"No product name in the message"

	def should_be_message_basket_price(self):
		assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_PRICE), (
			"Message basket total is not presented")
		assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), (
			"Product price is not presented")

		message_basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_PRICE).text
		item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
		assert "Your basket total is now {}".format(item_price) == "Your basket total is now {}".format(message_basket_price), \
			"No product price in the message"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.MESSAGE_BASKET_ITEM), \
			"Success message is presented, but should not be"

	def should_disappear_success_message(self):
		assert self.is_disappeared(*ProductPageLocators.MESSAGE_BASKET_ITEM), \
			"Success message has not disappeared, but should"

	def go_to_checkout(self):
		link = self.browser.find_element(*ProductPageLocators.CHECKOUT_BUTTON)
		link.click()

	def should_be_authorization_request(self):
		assert self.is_element_present(*CheckoutPageLocators.GUEST_CHECKOUT), (
			"Guest checkout option is not presented")
		assert self.is_element_present(*CheckoutPageLocators.NEW_USER_CHECKOUT), (
			"New user checkout option is not presented")
		assert self.is_element_present(*CheckoutPageLocators.USER_CHECKOUT), (
			"Existing user checkout option is not presented")
