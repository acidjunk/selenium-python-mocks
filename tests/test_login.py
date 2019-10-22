from unittest.mock import PropertyMock, patch

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from src.main import login


def test_login():
    # This test speeds up the login test by not waiting 10 seconds for the response.
    # As the improviser needs around a second to provide a stable error message for the
    # not existing user
    driver = webdriver.Chrome()
    with patch("time.sleep", return_value=None) as patched_time_sleep:
        with patch(
            "selenium.webdriver.remote.webdriver.WebDriver.page_source",
            new_callable=PropertyMock,
        ) as patched_page_source:
            # Fake the webdriver return with some content
            patched_page_source.return_value = (
                "Invalid credentials: Specified user does not exist"
            )
            login(driver)
    assert patched_time_sleep.call_count == 1
    assert patched_page_source.call_count == 1


def test_login_with_timeout():
    # This test checks what happens if the timeout regarding waiting for the login box to be clickable occurs
    driver = webdriver.Chrome()
    with patch("selenium.webdriver.support.wait.WebDriverWait.until") as patched_until:
        # Ensure that the Wait will always trigger the time out exception:
        patched_until.side_effect = TimeoutException("Timeout occured", None, None)
        login(driver)
    assert patched_until.call_count == 1
