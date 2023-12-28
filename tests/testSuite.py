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