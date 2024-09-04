import pytest
import time
from conftest import BASE_URL
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

SAMPLE_PRODUCT_LINK = f"{BASE_URL}/catalogue/coders-at-work_207/"
BASKET_LINK = f"{BASE_URL}/basket/"
LOGIN_URL = f"{BASE_URL}/accounts/login/"


# Test suite for not authorized user
@pytest.mark.guest_user
class TestGuestAddToCartFromProductPage:

    @pytest.mark.basket
    @pytest.mark.parametrize('product', ["coders-at-work_207",
                                         "applied-cryptography_200",
                                         "hacking-work_195"])
    def test_guest_can_add_product_to_cart(self, browser, product):
        link = f"{BASE_URL}/catalogue/{product}/"
        page = ProductPage(browser, link)
        self.add_product_to_basket(page)

    def add_product_to_basket(self, page):
        page.open()
        page.add_to_basket()
        page.should_be_message_basket_item()
        page.should_be_message_basket_price()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.login
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_LINK)
        page.open()
        page.should_be_login_link()

    @pytest.mark.login
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.basket
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_LINK)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_not_be_basket_items()

    @pytest.mark.basket
    def test_guest_cannot_purchase_without_logging_in(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_LINK)
        page.open()
        page.add_to_basket()
        page.go_to_checkout()
        page.should_be_authorization_request()

    @pytest.mark.basket
    def test_guest_cannot_access_checkout_without_products(self, browser):
        basket_page = BasketPage(browser, BASKET_LINK)
        basket_page.open()
        basket_page.should_not_have_checkout_option()


# Test suite for authorized user
@pytest.mark.registered_user
class TestUserAddToCartFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, generate_user_credentials):
        self.register_user(browser, generate_user_credentials)

    def register_user(self, browser, generate_user_credentials):
        register_page = LoginPage(browser, LOGIN_URL)
        register_page.open()
        credentials = generate_user_credentials
        register_page.register_new_user(credentials["email"], credentials["password"])
        register_page.should_be_authorized_user()

    @pytest.mark.basket
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_LINK)
        page.open()
        page.add_to_basket()
        page.should_be_message_basket_item()
        page.should_be_message_basket_price()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, SAMPLE_PRODUCT_LINK)
        page.open()
        page.should_not_be_success_message()
