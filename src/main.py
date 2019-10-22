import time

import structlog
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 5

logger = structlog.get_logger(__name__)


def python(driver):
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    time.sleep(TIMEOUT)
    assert "No results found." not in driver.page_source


def login(driver):
    # driver = webdriver.Chrome()
    driver.get("https://www.improviser.education/login")
    try:
        WebDriverWait(driver, TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="root"]/div/div[2]/div/div[2]/div/div/div/form/div/div[1]/div/input',
                )
            )
        ).send_keys("admin@example.com")
        WebDriverWait(driver, TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="root"]/div/div[2]/div/div[2]/div/div/div/form/div/div[2]/div/input',
                )
            )
        ).send_keys("some_password")
        WebDriverWait(driver, TIMEOUT).until(
            expected_conditions.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="root"]/div/div[2]/div/div[2]/div/div/div/form/div/button',
                )
            )
        ).click()
        # A time sleep(1) would have been enough: vamping it up to 10 for testing purposes
        time.sleep(10)
    except TimeoutException:
        logger.warning("Timeout occurred")
        return False
    assert "Invalid credentials: Specified user does not exist" in driver.page_source


if __name__ == "__main__":
    driver = webdriver.Chrome()
    python(driver)
    login(driver)
    driver.close()
