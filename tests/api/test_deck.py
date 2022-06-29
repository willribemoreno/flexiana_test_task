import deck_endpoints.deck_endpoints as deck_endpoints


# the same test is being performed here, but by different ways
def test_deck_creation_get_param_enabled():
    deck, status_code = deck_endpoints.create_deck_get_parameter(jokers_enabled=True)
    print(f'Status code: {status_code}')
    assert status_code == 200


# the same test is being performed here, but by different ways
def test_deck_creation_get_param_disabled():
    # print('deck creation get parameter disabled')
    deck, status_code = deck_endpoints.create_deck_get_parameter(jokers_enabled=False)
    print(f'Status code: {status_code}')
    assert status_code == 200


# the same test is being performed here, but by different ways
def test_deck_creation_post_parameter_enabled():
    deck, status_code = deck_endpoints.create_deck_post_parameter(jokers_enabled=True)
    print(f'Status code: {status_code}')
    assert status_code == 200


# the same test is being performed here, but by different ways
def test_deck_creation_post_parameter_disabled():
    deck, status_code = deck_endpoints.create_deck_post_parameter(jokers_enabled=False)
    print(f'Status code: {status_code}')
    assert status_code == 200


def test_reshuffle_cards():
    deck, deck_status_code = deck_endpoints.create_deck_get_parameter(jokers_enabled=True)
    print(f'Status code: {deck_status_code}')
    assert deck_status_code == 200

    reshuffle, status_code = deck_endpoints.reshuffle_deck(deck['deck_id'])
    print(f'Status code: {status_code}')
    assert status_code == 200


def test_draw_3_cards():
    deck, deck_status_code = deck_endpoints.create_deck_get_parameter(jokers_enabled=True)
    print(f'Status code: {deck_status_code}')
    assert deck_status_code == 200

    drawn_card, drawn_card_status_code = deck_endpoints.draw_cards(deck['deck_id'], 3)
    print(f'Status code: {drawn_card_status_code}')
    assert drawn_card_status_code == 200


def test_make_2_piles_with_5_cards_each_from_deck():
    deck, deck_status_code = deck_endpoints.create_deck_get_parameter(jokers_enabled=True)
    print(f'Status code: {deck_status_code}')
    assert deck_status_code == 200

    drawn_card, drawn_card_status_code = deck_endpoints.draw_cards(deck['deck_id'], 5)
    drawn_cards_list1 = deck_endpoints.get_drawn_card_codes(drawn_card)
    print(f'Status code: {drawn_card_status_code}')
    assert drawn_card_status_code == 200

    drawn_card2, drawn_card_status_code2 = deck_endpoints.draw_cards(deck['deck_id'], 5)
    drawn_cards_list2 = deck_endpoints.get_drawn_card_codes(drawn_card2)
    print(f'Status code: {drawn_card_status_code2}')
    assert drawn_card_status_code == 200

    pile1, pile1_status_code = deck_endpoints.add_to_pile(deck['deck_id'], 'pile1', drawn_cards_list1)
    print(f'Status code: {pile1_status_code}')
    assert pile1_status_code == 200
    print(pile1)

    pile2, pile2_status_code = deck_endpoints.add_to_pile(deck['deck_id'], 'pile2', drawn_cards_list2)
    print(f'Status code: {pile2_status_code}')
    assert pile2_status_code == 200
    print(pile2)


def test_list_the_cards_from_pile1_and_pile2():
    deck, deck_status_code = deck_endpoints.create_deck_get_parameter(jokers_enabled=True)
    print(f'Status code: {deck_status_code}')
    assert deck_status_code == 200

    drawn_card, drawn_card_status_code = deck_endpoints.draw_cards(deck['deck_id'], 5)
    drawn_cards_list1 = deck_endpoints.get_drawn_card_codes(drawn_card)
    print(f'Status code: {drawn_card_status_code}')
    assert drawn_card_status_code == 200

    drawn_card2, drawn_card_status_code2 = deck_endpoints.draw_cards(deck['deck_id'], 5)
    drawn_cards_list2 = deck_endpoints.get_drawn_card_codes(drawn_card2)
    print(f'Status code: {drawn_card_status_code2}')
    assert drawn_card_status_code == 200

    pile1, pile1_status_code = deck_endpoints.add_to_pile(deck['deck_id'], 'pile1', drawn_cards_list1)
    print(f'Status code: {pile1_status_code}')
    assert pile1_status_code == 200
    print(pile1)

    pile2, pile2_status_code = deck_endpoints.add_to_pile(deck['deck_id'], 'pile2', drawn_cards_list2)
    print(f'Status code: {pile2_status_code}')
    assert pile2_status_code == 200
    print(pile2)

    pile1_list, pile1_list_status_code = deck_endpoints.list_card_from_pile(deck['deck_id'], 'pile1')
    print(f'Status code: {pile1_list_status_code}')
    assert pile1_list_status_code == 200
    print(pile1_list)

    pile2_list, pile2_list_status_code = deck_endpoints.list_card_from_pile(deck['deck_id'], 'pile2')
    print(f'Status code: {pile2_list_status_code}')
    assert pile2_list_status_code == 200
    print(pile2_list)


def test_shuffle_pile1():
    deck, deck_status_code = deck_endpoints.create_deck_get_parameter(jokers_enabled=True)
    print(f'Status code: {deck_status_code}')
    assert deck_status_code == 200

    drawn_card, drawn_card_status_code = deck_endpoints.draw_cards(deck['deck_id'], 5)
    drawn_cards_list1 = deck_endpoints.get_drawn_card_codes(drawn_card)
    print(f'Status code: {drawn_card_status_code}')
    assert drawn_card_status_code == 200

    pile1, pile1_status_code = deck_endpoints.add_to_pile(deck['deck_id'], 'pile1', drawn_cards_list1)
    print(f'Status code: {pile1_status_code}')
    assert pile1_status_code == 200
    print(pile1)

    pile1_list, pile1_list_status_code = deck_endpoints.list_card_from_pile(deck['deck_id'], 'pile1')
    print(f'Status code: {pile1_list_status_code}')
    assert pile1_list_status_code == 200
    print(pile1_list)

    shuffle_pile1, shuffle_pile1_status_code = deck_endpoints.shuffle_pile(deck['deck_id'], 'pile1')
    print(f'Status code: {shuffle_pile1_status_code}')
    print(shuffle_pile1)


def test_draw_2_cards_from_pile1():
    deck, deck_status_code = deck_endpoints.create_deck_get_parameter(jokers_enabled=True)
    print(f'Status code: {deck_status_code}')
    assert deck_status_code == 200

    drawn_card, drawn_card_status_code = deck_endpoints.draw_cards(deck['deck_id'], 5)
    drawn_cards_list1 = deck_endpoints.get_drawn_card_codes(drawn_card)
    print(f'Status code: {drawn_card_status_code}')
    assert drawn_card_status_code == 200

    drawn_card2, drawn_card_status_code2 = deck_endpoints.draw_cards(deck['deck_id'], 5)
    drawn_cards_list2 = deck_endpoints.get_drawn_card_codes(drawn_card2)
    print(f'Status code: {drawn_card_status_code2}')
    assert drawn_card_status_code == 200

    pile1, pile1_status_code = deck_endpoints.add_to_pile(deck['deck_id'], 'pile1', drawn_cards_list1)
    print(f'Status code: {pile1_status_code}')
    assert pile1_status_code == 200
    print(pile1)

    pile2, pile2_status_code = deck_endpoints.add_to_pile(deck['deck_id'], 'pile2', drawn_cards_list2)
    print(f'Status code: {pile2_status_code}')
    assert pile2_status_code == 200
    print(pile2)

    shuffle_pile1, shuffle_pile1_status_code = deck_endpoints.drawing_from_pile(deck['deck_id'], 'pile1', count=2)
    print(f'Status code: {shuffle_pile1_status_code}')
    print(shuffle_pile1)


def test_draw_3_cards_from_pile2():
    deck, deck_status_code = deck_endpoints.create_deck_get_parameter(jokers_enabled=True)
    print(f'Status code: {deck_status_code}')
    assert deck_status_code == 200

    drawn_card, drawn_card_status_code = deck_endpoints.draw_cards(deck['deck_id'], 5)
    drawn_cards_list1 = deck_endpoints.get_drawn_card_codes(drawn_card)
    print(f'Status code: {drawn_card_status_code}')
    assert drawn_card_status_code == 200

    drawn_card2, drawn_card_status_code2 = deck_endpoints.draw_cards(deck['deck_id'], 5)
    drawn_cards_list2 = deck_endpoints.get_drawn_card_codes(drawn_card2)
    print(f'Status code: {drawn_card_status_code2}')
    assert drawn_card_status_code == 200

    pile1, pile1_status_code = deck_endpoints.add_to_pile(deck['deck_id'], 'pile1', drawn_cards_list1)
    print(f'Status code: {pile1_status_code}')
    assert pile1_status_code == 200
    print(pile1)

    pile2, pile2_status_code = deck_endpoints.add_to_pile(deck['deck_id'], 'pile2', drawn_cards_list2)
    print(f'Status code: {pile2_status_code}')
    assert pile2_status_code == 200
    print(pile2)

    shuffle_pile2, shuffle_pile2_status_code = deck_endpoints.drawing_from_pile(deck['deck_id'], 'pile2', count=3)
    print(f'Status code: {shuffle_pile2_status_code}')
    print(shuffle_pile2)
