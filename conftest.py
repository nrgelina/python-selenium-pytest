import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import logging

logger = logging.getLogger(__name__)

BASE_URL = "http://selenium1py.pythonanywhere.com/"


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, es, etc.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if browser_name == "chrome":
        logger.info("Starting chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        logger.info("Starting firefox browser for test..")
        fp = FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        logger.info(f"Browser {browser_name} is not implemented yet")
    browser.implicitly_wait(5)
    yield browser
    logger.info("Quitting browser")
    browser.quit()


@pytest.fixture
def generate_user_credentials():
    email = str(time.time()) + "@fakemail.org"
    password = "123test123"
    return {"email": email, "password": password}
