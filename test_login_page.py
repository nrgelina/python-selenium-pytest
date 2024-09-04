import time

from conftest import BASE_URL
from pages.login_page import LoginPage
import pytest

LOGIN_URL = f"{BASE_URL}/accounts/login/"


@pytest.mark.login
class TestLoginPage:

	def test_login_page(self, browser):
		page = LoginPage(browser, LOGIN_URL)
		page.open()
		page.should_be_login_page()

	def test_successful_login(self, browser, generate_user_credentials):
		page = LoginPage(browser, LOGIN_URL)
		page.open()
		credentials = generate_user_credentials
		page.register_new_user(credentials["email"], credentials["password"])
		page.logout()

		page = LoginPage(browser, LOGIN_URL)
		page.open()
		page.login(credentials["email"], credentials["password"])
		page.should_be_authorized_user()

	def test_unsuccessful_login(self, browser, generate_user_credentials):
		page = LoginPage(browser, LOGIN_URL)
		page.open()
		credentials = generate_user_credentials
		page.login(credentials["email"], credentials["password"])
		page.should_be_login_error_message()

	@pytest.mark.xfail(reason="logging in with empty credentials does not raise an error message")
	def test_login_with_empty_credentials(self, browser):
		page = LoginPage(browser, LOGIN_URL)
		page.open()
		page.login("", "")
		page.should_be_login_error_message()
