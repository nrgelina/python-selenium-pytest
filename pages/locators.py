from selenium.webdriver.common.by import By


class BasePageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_BUTTON = (By.LINK_TEXT, "View basket")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(object):
	pass


class LoginPageLocators(object):
	LOGIN_FORM = (By.ID, "login_form")
	LOGIN_EMAIL = (By.NAME, "login-username")
	LOGIN_PASSWORD = (By.NAME, "login-password")
	LOGIN_BUTTON = (By.NAME, "login_submit")
	LOGOUT_BUTTON = (By.ID, "logout_link")
	LOGIN_ERROR_ALERT = (By.CSS_SELECTOR, ".alert-danger")
	REGISTER_FORM = (By.ID, "register_form")
	REGISTRATION_EMAIL = (By.NAME, "registration-email")
	REGISTRATION_PASSWORD = (By.NAME, "registration-password1")
	CONFIRM_PASSWORD = (By.NAME, "registration-password2")
	REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators(object):
	ADD_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
	MESSAGE_BASKET_ITEM = (By.CSS_SELECTOR, "div.alertinner ")
	MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
	ITEM_NAME = (By.CSS_SELECTOR, "div.product_main h1")
	ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	CHECKOUT_BUTTON = (By.LINK_TEXT, "Checkout now")


class BasketPageLocators(object):
	BASKET_EMPTY_TEXT = (By.ID, "content_inner")
	BASKET_ITEM = (By.CLASS_NAME, "basket-items")
	CHECKOUT_BUTTON = (By.LINK_TEXT, "Proceed to checkout")


class CheckoutPageLocators(object):
	GUEST_CHECKOUT = (By.ID, "id_options_0")
	NEW_USER_CHECKOUT = (By.ID, "id_options_1")
	USER_CHECKOUT = (By.ID, "id_options_2")
