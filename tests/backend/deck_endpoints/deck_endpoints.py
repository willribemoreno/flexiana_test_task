import requests
import re

# class DeckCalls:

_BASE_URL = 'http://deckofcardsapi.com/api/deck/'


def create_deck_get_parameter(jokers_enabled=False):
    API = _BASE_URL + 'new/'
    if jokers_enabled:
        API += '?jokers_enabled=true'
    url = API.format(jokers_enabled=jokers_enabled)

    response = requests.get(url)
    return response.json(), response.status_code


def create_deck_post_parameter(jokers_enabled=False):
    API = _BASE_URL + 'new'
    params = None
    url = API.format(jokers_enabled=jokers_enabled)
    if jokers_enabled:
        params = {'jokers_enabled': 'true'}
    response = requests.get(url, params)
    return response.json(), response.status_code


def shuffle_deck(deck_qty):
    """ Deck creation """
    API = _BASE_URL + 'new/shuffle/?deck_count={count_value}'
    url = API.format(count_value=deck_qty)
    response = requests.get(url)
    return response.json(), response.status_code


def reshuffle_deck(deck_id, **kwargs):
    """ Deck creation """
    param = None
    API = _BASE_URL + '{deck_id}/shuffle/?remaining=true'
    url = API.format(deck_id=deck_id)
    if kwargs:
        param[kwargs]
    response = requests.get(url, param)
    return response.json(), response.status_code


def draw_cards(deck_id, count):
    API = _BASE_URL + '{deck_id}/draw/?count={count}'
    url = API.format(deck_id=deck_id, count=count)
    response = requests.get(url)
    return response.json(), response.status_code


def get_drawn_card_codes(drawn_card_obj):
    cards = []
    for key, value in drawn_card_obj.items():
        if key == 'cards':
            for card in value:
                cards.append(card['code'])
    cards = re.sub(r'[][\' ]', '', str(cards))
    return cards


def add_to_pile(deck_id, pile_name, drawn_cards):
    API = _BASE_URL + '{deck_id}/pile/{pile_name}/add/?cards={drawn_cards}'
    url = API.format(deck_id=deck_id, pile_name=pile_name, drawn_cards=drawn_cards)
    response = requests.get(url)
    return response.json(), response.status_code


def list_card_from_pile(deck_id, pile_name):
    API = _BASE_URL + '{deck_id}/pile/{pile_name}/list/'
    url = API.format(deck_id=deck_id, pile_name=pile_name)
    response = requests.get(url)
    return response.json(), response.status_code


def shuffle_pile(deck_id, pile_name):
    API = _BASE_URL + '{deck_id}/pile/{pile_name}/shuffle/'
    url = API.format(deck_id=deck_id, pile_name=pile_name)
    response = requests.get(url)
    return response.json(), response.status_code


def drawing_from_pile(deck_id, pile_name, count=None, cards=None, bottom=None, random=None):

    if count:
        API = _BASE_URL + '{deck_id}/pile/{pile_name}/draw/?count={count}'
        url = API.format(deck_id=deck_id, pile_name=pile_name, count=count)
    if cards:
        API = _BASE_URL + '{deck_id}/pile/{pile_name}/draw/?cards={cards}'
        url = API.format(deck_id=deck_id, pile_name=pile_name, cards=cards)
    if bottom:
        API = _BASE_URL + '{deck_id}/draw/bottom/'
        url = API.format(deck_id=deck_id)
    if random:
        API = _BASE_URL + '{deck_id}/draw/random/'
        url = API.format(deck_id=deck_id)

    response = requests.get(url)
    return response.json(), response.status_code
