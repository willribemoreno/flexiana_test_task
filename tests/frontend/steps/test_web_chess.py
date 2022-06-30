import time

from pytest_bdd import scenarios, given, when, then
from tests.frontend.web.pages.home import HomePage as home
from tests.frontend.web.pages.privacy_banner import PrivacyBannerPage as privacy_banner

scenarios('../features/checkers.feature')


@given('the user is in the home page')
def step_impl(driver):
    if privacy_banner.is_on_focus(driver):
        privacy_banner.exit_page(driver)
    home.is_on_focus(driver)


@when('he starts a new game by clicking on restart button')
@given('he starts a new game by clicking on restart button')
def step_impl(driver):
    home.click_on_restart_btn(driver)


@then('all pieces must be returned to original place')
def step_impl(driver):
    home.check_if_pieces_were_moved_to_default_position(driver)


@given('he makes his first move')
@when('he makes his first move')
def step_impl(driver, from_to_moves_orange):
    home.make_first_move(driver, from_to_moves_orange)


@then('the users piece must be moved properly')
def step_impl(driver, from_to_moves_orange):
    home.assert_moves(driver, from_to_moves_orange, move_count=1)


@when('the computer makes his move')
def step_impl():
    time.sleep(2)
    pass


@then('the computer piece must be moved properly')
def step_impl(driver, from_to_moves_blue):
    home.check_if_computer_piece_was_moved(driver, from_to_moves_blue, move_count=1)


@when('he makes his second move')
def step_impl(driver, from_to_moves_orange):
    coordinates = (6, 4)
    home.make_move(driver, from_to_moves_orange, move_count=2, new_coordinates=coordinates)
