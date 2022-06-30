from enum import Enum

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Browser(Enum):
    """ Browser names """

    CHROME = 'chrome'
    EDGE = 'edge'
    FIREFOX = 'firefox'
    SAFARI = 'safari'


_LOCAL_BROWSER_DRIVER_MAP = {
    Browser.CHROME.value: (Chrome, ChromeDriverManager, ChromeService)
    }


def web_driver_factory(chosen_browser, browserstack=False):
    """

    :param chosen_browser: str
        The name of the chosen driver e.g firefox
    :param browserstack: bool
        The condition to check if it will be a BS execution
    :return:
    """

    # defensive programming in order to check if the passed parameter type is as expected
    if not isinstance(chosen_browser, (str, Enum)):
        raise ValueError('The "chosen_browser" variable type must be string or enum')

    base_cls, driver_manager_custom, driver_service_custom = _LOCAL_BROWSER_DRIVER_MAP[chosen_browser]

    class CustomRemoteWebDriver(base_cls):
        params = dict()
        params.update(dict(service=driver_service_custom(driver_manager_custom().install())))

        def __init__(self, desired_capabilities):
            super().__init__(**self.params)

    return CustomRemoteWebDriver


def get_driver_custom(browser_name):

    class GetDriver(web_driver_factory(browser_name)):
        def __init__(self):
            super().__init__(desired_capabilities=None)

    return GetDriver()
