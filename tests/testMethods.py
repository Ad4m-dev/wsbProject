import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class HolidayPageTests:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.tui.pl"
        self.driver.implicitly_wait(10)
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def open_page(self):
        self.driver.get(self.url)

        # Check if right page is opened
        assert "tui.pl" in self.driver.current_url, "Correct page not opened"

    def accept_rodo_agreement(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='CybotCookiebotDialog']/div"))
            )
            button_accept = self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
            button_accept.click()

        except Exception as e:
            error_message = e.args[0] if e.args else "No error message provided"
            pytest.fail(f"Test failed: {error_message}")