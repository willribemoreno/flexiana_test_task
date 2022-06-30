import pytest
from core.driver import get_driver_custom


@pytest.fixture(scope='function')
def driver():
    driver = get_driver_custom('chrome')
    driver.get('https://www.gamesforthebrain.com/game/checkers/')
    driver.maximize_window()
    yield driver


@pytest.fixture(scope='session')
def from_to_moves_blue():
    return {}


@pytest.fixture(scope='session')
def from_to_moves_orange():
    return {}


def pytest_bdd_after_scenario(request):
    # Add things to be done after each test scenario here
    driver = request.getfixturevalue('driver')
    driver.close()
