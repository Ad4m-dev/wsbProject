import pytest
from selenium import webdriver
from testMethods import HolidayPageTests


# Create a "fixture" for the browser to make it available to all tests.
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    holiday_page = HolidayPageTests(driver)
    yield holiday_page
    driver.quit()


# Test open page
def test_open_page(browser):
    browser.open_page()
    browser.accept_rodo_agreement()


# Test try to log without email
def test_login_without_email(browser):
    browser.open_login_page()
    browser.missing_email()
    browser.is_missing_email_failed()


# Test try to log without password
def test_login_without_password(browser):
    browser.enter_email()
    browser.missing_password()
    browser.is_missing_password_failed()