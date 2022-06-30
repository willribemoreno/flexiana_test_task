import time

from ..mapping.home import HomeMapping as mapping
from core.web_actions import WebActions
import re
import random


class HomePage:

    @staticmethod
    def is_on_focus(driver):
        web_actions = WebActions(driver)
        return all([web_actions.wait_until_element_visible(mapping.TBL_BOARD),
                    web_actions.wait_until_element_visible(mapping.TxT_HEADER)])

    @staticmethod
    def click_on_restart_btn(driver):
        web_actions = WebActions(driver)
        web_actions.wait_until_element_clickable(mapping.BTN_RESTART).click()

    @staticmethod
    def check_if_pieces_were_moved_to_default_position(driver):
        web_actions = WebActions(driver)
        new_blue_position_list = web_actions.wait_until_elements_visible(mapping.IMG_BLUE_PIECES)
        default_blue_position = ['didClick(7, 7)', 'didClick(5, 7)', 'didClick(3, 7)', 'didClick(1, 7)',
                                 'didClick(6, 6)', 'didClick(4, 6)', 'didClick(2, 6)', 'didClick(0, 6)',
                                 'didClick(7, 5)', 'didClick(5, 5)', 'didClick(3, 5)', 'didClick(1, 5)']
        new_orange_position_list = web_actions.wait_until_elements_visible(mapping.IMG_ORANGE_PIECES)
        default_orange_position = ['didClick(6, 2)', 'didClick(4, 2)', 'didClick(2, 2)', 'didClick(0, 2)',
                                   'didClick(7, 1)', 'didClick(5, 1)', 'didClick(3, 1)', 'didClick(1, 1)',
                                   'didClick(6, 0)', 'didClick(4, 0)', 'didClick(2, 0)', 'didClick(0, 0)']

        orange_comparison_list = HomePage.compare_default_new_piece_positions(
            default_blue_position, new_blue_position_list)
        blue_comparison_list = HomePage.compare_default_new_piece_positions(
            default_orange_position, new_orange_position_list)
        assert len(orange_comparison_list) == 0, f'Comparison failed, please, check not matching positions: ' \
                                                 f'{orange_comparison_list}'
        assert len(blue_comparison_list) == 0, f'Comparison failed, please, check not matching positions: ' \
                                               f'{blue_comparison_list}'

    @staticmethod
    def compare_default_new_piece_positions(default_position, new_positions):
        not_matching_list = []
        for index_default in range(len(default_position)):
            for index_new in range(len(new_positions)):
                if default_position[index_default] == new_positions[index_new].get_attribute('onclick'):
                    break
                if index_new == len(new_positions) - 1:
                    # if the method workflow comes here, it means that object in index_new position did not matched
                    # with any default value, thus, it's not in default position
                    not_matching_list.append(default_position[index_default])
        # if not_matching_list list has any value, it means that there a peace in a not default position
        return not_matching_list

    @staticmethod
    def make_first_move(driver, from_to_moves_orange):
        move_count = 1
        x = 4
        y = 2
        x_new = 5
        y_new = 3
        web_actions = WebActions(driver)
        orange_pieces = web_actions.wait_until_elements_visible(mapping.IMG_ORANGE_PIECES)
        chosen_move, available_moves, available_gray_slot_pos_dict = HomePage.possible_moves(
            driver, piece_to_move_coordinates=(x, y))
        chosen_move = '{x}, {y}'.format(x=x_new, y=y_new)

        for piece in orange_pieces:
            if piece.get_attribute('onclick') == 'didClick({x}, {y})'.format(x=x, y=y):
                piece.click()
                break

        available_gray_slot_pos_dict[chosen_move].click()
        if 'from' in from_to_moves_orange.keys():
            from_to_moves_orange['from'].update({move_count: f'{x}, {y}'})
        else:
            from_to_moves_orange['from'] = {move_count: f'{x}, {y}'}
        if 'to' in from_to_moves_orange.keys():
            from_to_moves_orange['to'].update({move_count: chosen_move})
        else:
            from_to_moves_orange['to'] = {move_count: chosen_move}

    @staticmethod
    def make_move(driver, from_to_moves_orange, move_count, coordinates=None, new_coordinates=None):
        time.sleep(2)
        if new_coordinates and move_count > 1:
            x_new, y_new = new_coordinates
        if not coordinates and move_count > 1:
            x, y = from_to_moves_orange['to'][move_count - 1].split()
            x = re.sub(r'[,]', '', x)
            y = re.sub(r'[,]', '', y)
            x = int(x)
            y = int(y)
        else:
            x, y = coordinates
        web_actions = WebActions(driver)
        orange_pieces = web_actions.wait_until_elements_visible(mapping.IMG_ORANGE_PIECES)
        chosen_move, available_moves, available_gray_slot_pos_dict = HomePage.possible_moves(
            driver, piece_to_move_coordinates=(x, y))
        if new_coordinates:
            chosen_move = '{x}, {y}'.format(x=x_new, y=y_new)
        for piece in orange_pieces:
            if piece.get_attribute('onclick') == 'didClick({x}, {y})'.format(x=x, y=y):
                piece.click()
                break

        available_gray_slot_pos_dict[chosen_move].click()
        if 'from' in from_to_moves_orange.keys():
            from_to_moves_orange['from'].update({move_count: f'{x}, {y}'})
        else:
            from_to_moves_orange['from'] = {move_count: f'{x}, {y}'}

        if 'to' in from_to_moves_orange.keys():
            from_to_moves_orange['to'].update({move_count: chosen_move})
        else:
            from_to_moves_orange['to'] = {move_count: chosen_move}

    @staticmethod
    def create_position_x_element_dict(element):
        position_x_element_dict = {}
        if element[0].get_attribute('onclick'):
            for el in element:
                onclick_str = el.get_attribute('onclick')
                new_onclick_str = str(re.findall(r'([0-7]...)', onclick_str))
                new_onclick_str = re.sub(r"[\][']", "", new_onclick_str)
                position_x_element_dict[f'{new_onclick_str}'] = el
        else:
            for el in element:
                name_attr_str = el.get_attribute('name')
                new_name_str = str(re.findall(r'([0-7].)', name_attr_str))
                new_name_attr_str = re.sub(r"[\][']", "", new_name_str)
                new_name_attr_str = re.sub(r'(\d)(\d)', r'\1,\2', new_name_attr_str)
                position_x_element_dict[f'{new_name_attr_str}'] = el

        return position_x_element_dict

    @staticmethod
    def possible_moves(driver, piece_to_move_coordinates, random_choose=False):
        """ checks the possible moves for an specific piece

            :param driver: WebDriver
                The Selenium WebDriver element
            :param piece_to_move_coordinates: tuple
                A coordinate where you want to move to
                e.g (5, 3)
            :param random_choose: bool
                A boolean to check if the chosen_move will returns a fixed or random value
        """
        available_moves = []
        web_actions = WebActions(driver)
        available_gray_coordinates = web_actions.wait_until_elements_visible(mapping.IMG_AVAILABLE_GRAY_POSITIONS)
        available_gray_slot_pos_dict = HomePage.create_position_x_element_dict(available_gray_coordinates)
        x, y = piece_to_move_coordinates
        possible_moves = [f'{x + 1}, {y + 1}', f'{x + 1}, {y - 1}', f'{x - 1}, {y + 1}', f'{x - 1}, {y - 1}']
        for coordinate in possible_moves:
            if coordinate in available_gray_slot_pos_dict.keys():
                available_moves.append(coordinate)
        if len(available_moves) == 0:
            raise ValueError(f'The received coordinates has no available moves: x: {x}, y: {y}')
        # random used to always tries a different move
        if random_choose:
            chosen_move_index = random.randint(0, len(available_moves) - 1)
        else:
            chosen_move_index = 0
        chosen_move = available_moves[chosen_move_index]
        return chosen_move, available_moves, available_gray_slot_pos_dict

    @staticmethod
    def assert_moves(driver, from_to_moves_orange, move_count):
        # this explicit waiting is necessary in order to wait till the board has the new values after the move
        time.sleep(2)
        web_actions = WebActions(driver)
        orange_pieces = web_actions.wait_until_elements_visible(mapping.IMG_ORANGE_PIECES)
        orange_pieces_dict = HomePage.create_position_x_element_dict(orange_pieces)
        available_gray_coordinates = web_actions.wait_until_elements_visible(mapping.IMG_AVAILABLE_GRAY_POSITIONS)
        available_gray_slot_pos_dict = HomePage.create_position_x_element_dict(available_gray_coordinates)

        assert from_to_moves_orange['from'][move_count] in available_gray_slot_pos_dict.keys()
        if move_count >= 2:
            # if counter is more than 2, the computer was already take the user's piece
            assert from_to_moves_orange['to'][move_count] not in orange_pieces_dict.keys()
        else:
            assert from_to_moves_orange['to'][move_count] in orange_pieces_dict.keys()

    @staticmethod
    def check_if_computer_piece_was_moved(driver, from_to_moves_blue, move_count):
        """" Checks if blue pieces in no longer in the default positions
            :param driver: WebDriver
                The WebDriver instance
            :param from_to_moves_blue: dict
                The dict of movements performed in blue pieces
            :param move_count: int
                The movements counter. Use it to get the from/to values of specific movement
                e.g 2
        """
        time.sleep(2)
        x = None
        y = None
        possible_moves_available = []
        default_blue_position = ['didClick(7, 7)', 'didClick(5, 7)', 'didClick(3, 7)', 'didClick(1, 7)',
                                 'didClick(6, 6)', 'didClick(4, 6)', 'didClick(2, 6)', 'didClick(0, 6)',
                                 'didClick(7, 5)', 'didClick(5, 5)', 'didClick(3, 5)', 'didClick(1, 5)']
        web_actions = WebActions(driver)
        default_gray_positions = ['didClick(6, 4)', 'didClick(4, 4)', 'didClick(2, 4)', 'didClick(0, 4)',
                                  'didClick(7, 3)', 'didClick(5, 3)', 'didClick(3, 3)', 'didClick(1, 3)']
        new_blue_position_list = web_actions.wait_until_elements_visible(mapping.IMG_BLUE_PIECES)
        blue_pos_dict = HomePage.create_position_x_element_dict(new_blue_position_list)

        # checks which blue piece default position no longer exists
        for index_default in range(len(default_blue_position)):
            new_default_pos = str(re.findall(r'([0-7]...)', default_blue_position[index_default]))
            new_default_pos = re.sub(r"[\][']", "", new_default_pos)
            for index_actual in range(len(blue_pos_dict)):
                if new_default_pos in blue_pos_dict.keys():
                    break
                if index_actual == len(blue_pos_dict) - 1:
                    if 'from' in from_to_moves_blue.keys():
                        from_to_moves_blue['from'].update({move_count: new_default_pos})
                    else:
                        from_to_moves_blue['from'] = {move_count: new_default_pos}

        for from_move in from_to_moves_blue['from'].keys():
            if from_move == move_count:
                x, y = from_to_moves_blue['from'][from_move].split()

        x = re.sub(r'[,]', '', x)
        y = re.sub(r'[,]', '', y)
        x = int(x)
        y = int(y)
        possible_moves = [f'{x + 1}, {y + 1}', f'{x + 1}, {y - 1}', f'{x - 1}, {y + 1}', f'{x - 1}, {y - 1}']

        # filter possible moves of moved piece and checks which moves was available in default position
        for index in range(len(possible_moves)):
            for index2 in range(len(default_gray_positions)):
                new_default_pos = str(re.findall(r'([0-7]...)', default_gray_positions[index2]))
                new_default_pos = re.sub(r"[\][']", "", new_default_pos)
                if possible_moves[index] in new_default_pos:
                    possible_moves_available.append(possible_moves[index])

        for index in range(len(possible_moves_available)):
            if possible_moves_available[index] in blue_pos_dict.keys():
                if 'to' in from_to_moves_blue.keys():
                    from_to_moves_blue['to'].update({move_count: possible_moves_available[index]})
                else:
                    from_to_moves_blue['to'] = {move_count: possible_moves_available[index]}
                break

        # once we have the from / to keys in from_to_moves_blue dict, the piece were moved properly
        assert move_count in from_to_moves_blue['from'].keys()
        assert move_count in from_to_moves_blue['to'].keys()

    @staticmethod
    def assert_taken_piece_removal(driver, from_to_moves_orange, count):
        removed_piece_coordinate = from_to_moves_orange['to'][count]
        web_actions = WebActions(driver)
        orange_pieces = web_actions.wait_until_elements_visible(mapping.IMG_ORANGE_PIECES)
        orange_pieces_dict = HomePage.create_position_x_element_dict(orange_pieces)

        assert removed_piece_coordinate not in orange_pieces_dict.keys()
        # once one piece has been taken, must have only eleven orange pieces in the board
        assert len(orange_pieces_dict) == 11
