import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class WebActions:

    def __init__(self, driver):
        self._driver = driver

    def wait_until_element_clickable(self, locator, timeout=10):
        """ If the element is clickable returns a unique WebElement """
        timeout = 5 if not timeout else timeout
        driver_wait = WebDriverWait(driver=self._driver, timeout=timeout)
        return driver_wait.until(expected_conditions.element_to_be_clickable(locator),
                                 message=f'Element not clickable after {timeout} seconds')

    def wait_until_element_visible(self, locator, timeout=10):
        """ If the element is visible returns a unique WebElement """
        timeout = 5 if not timeout else timeout
        driver_wait = WebDriverWait(driver=self._driver, timeout=timeout)
        return driver_wait.until(expected_conditions.visibility_of_element_located(locator),
                                 message=f'Element not visible after {timeout} seconds')

    def wait_until_elements_visible(self, locator, timeout=10):
        """ If all elements are visible returns a WebElement list """
        timeout = 5 if not timeout else timeout
        driver_wait = WebDriverWait(driver=self._driver, timeout=timeout)
        return driver_wait.until(expected_conditions.visibility_of_all_elements_located(locator),
                                 message=f'Element not clickable after {timeout} seconds')
