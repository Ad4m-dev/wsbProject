import datetime
import os


def make_screenshot(driver, screenshot_name):
    today = datetime.datetime.today()
    short_date = today.strftime("%H:%M:%S")

    # Set the directory path
    screenshot_directory = '/home/adam/PycharmProjects/wsbProject/tests/screens'

    # Check if the directory exists (if not, create a new directory)
    if not os.path.exists(screenshot_directory):
        os.makedirs(screenshot_directory)

    # The full path name with screenshot
    screenshot_path = os.path.join(screenshot_directory, f'{screenshot_name}_{short_date}.png')

    # Save the screenshot in right place
    driver.get_screenshot_as_file(screenshot_path)

