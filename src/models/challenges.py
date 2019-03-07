# NEED TO REFACTOR


def challenges(game, played_card, selected_position, current_player, P1, P2):
    if selected_position == 'top_left':
        __top_left_placement(game, played_card, current_player, P1, P2)
    if selected_position == 'top_center':
        __top_center_placement(game, played_card, current_player, P1, P2)
    if selected_position == 'top_right':
        __top_right_placement(game, played_card, current_player, P1, P2)
    if selected_position == 'mid_left':
        __mid_left_placement(game, played_card, current_player, P1, P2)
    if selected_position == 'mid_center':
        __mid_center_placement(game, played_card, current_player, P1, P2)
    if selected_position == 'mid_right':
        __mid_right_placement(game, played_card, current_player, P1, P2)
    if selected_position == 'bot_left':
        __bot_left_placement(game, played_card, current_player, P1, P2)
    if selected_position == 'bot_center':
        __bot_center_placement(game, played_card, current_player, P1, P2)
    if selected_position == 'bot_right':
        __bot_right_placement(game, played_card, current_player, P1, P2)


def __top_left_placement(game, played_card, current_player, P1, P2):
    if game.positions['top_center']['card'] is not None and played_card['r_value'] > game.positions['top_center']['card']['l_value']:
        __flip_owner(game.positions['top_center'], current_player, P1, P2)
    if game.positions['mid_left']['card'] is not None and played_card['b_value'] > game.positions['mid_left']['card']['t_value']:
        __flip_owner(game.positions['mid_left'], current_player, P1, P2)


def __top_center_placement(game, played_card, current_player, P1, P2):
    if game.positions['top_left']['card'] is not None and played_card['l_value'] > game.positions['top_left']['card']['r_value']:
        __flip_owner(game.positions['top_left'], current_player, P1, P2)
    if game.positions['top_right']['card'] is not None and played_card['r_value'] > game.positions['top_right']['card']['l_value']:
        __flip_owner(game.positions['top_right'], current_player, P1, P2)
    if game.positions['mid_center']['card'] is not None and played_card['b_value'] > game.positions['mid_center']['card']['t_value']:
        __flip_owner(game.positions['mid_center'], current_player, P1, P2)


def __top_right_placement(game, played_card, current_player, P1, P2):
    if game.positions['top_center']['card'] is not None and played_card['l_value'] > game.positions['top_center']['card']['r_value']:
        __flip_owner(game.positions['top_center'], current_player, P1, P2)
    if game.positions['mid_right']['card'] is not None and played_card['b_value'] > game.positions['mid_right']['card']['t_value']:
        __flip_owner(game.positions['mid_right'], current_player, P1, P2)


def __mid_left_placement(game, played_card, current_player, P1, P2):
    if game.positions['top_left']['card'] is not None and played_card['t_value'] > game.positions['top_left']['card']['b_value']:
        __flip_owner(game.positions['top_left'], current_player, P1, P2)
    if game.positions['bot_left']['card'] is not None and played_card['b_value'] > game.positions['bot_left']['card']['t_value']:
        __flip_owner(game.positions['bot_left'], current_player, P1, P2)
    if game.positions['mid_center']['card'] is not None and played_card['r_value'] > game.positions['mid_center']['card']['l_value']:
        __flip_owner(game.positions['mid_center'], current_player, P1, P2)


def __mid_center_placement(game, played_card, current_player, P1, P2):
    if game.positions['top_center']['card'] is not None and played_card['t_value'] > game.positions['top_center']['card']['b_value']:
        __flip_owner(game.positions['top_center'], current_player, P1, P2)
    if game.positions['bot_center']['card'] is not None and played_card['b_value'] > game.positions['bot_center']['card']['t_value']:
        __flip_owner(game.positions['bot_center'], current_player, P1, P2)
    if game.positions['mid_left']['card'] is not None and played_card['l_value'] > game.positions['mid_left']['card']['r_value']:
        __flip_owner(game.positions['mid_left'], current_player, P1, P2)
    if game.positions['mid_right']['card'] is not None and played_card['r_value'] > game.positions['mid_right']['card']['l_value']:
        __flip_owner(game.positions['mid_right'], current_player, P1, P2)


def __mid_right_placement(game, played_card, current_player, P1, P2):
    if game.positions['top_right']['card'] is not None and played_card['t_value'] > game.positions['top_right']['card']['b_value']:
        __flip_owner(game.positions['top_right'], current_player, P1, P2)
    if game.positions['bot_right']['card'] is not None and played_card['b_value'] > game.positions['bot_right']['card']['t_value']:
        __flip_owner(game.positions['bot_right'], current_player, P1, P2)
    if game.positions['mid_center']['card'] is not None and played_card['l_value'] > game.positions['mid_center']['card']['r_value']:
        __flip_owner(game.positions['mid_center'], current_player, P1, P2)


def __bot_left_placement(game, played_card, current_player, P1, P2):
    if game.positions['bot_center']['card'] is not None and played_card['r_value'] > game.positions['bot_center']['card']['l_value']:
        __flip_owner(game.positions['bot_center'], current_player, P1, P2)
    if game.positions['mid_left']['card'] is not None and played_card['t_value'] > game.positions['mid_left']['card']['b_value']:
        __flip_owner(game.positions['mid_left'], current_player, P1, P2)


def __bot_center_placement(game, played_card, current_player, P1, P2):
    if game.positions['bot_left']['card'] is not None and played_card['l_value'] > game.positions['bot_left']['card']['r_value']:
        __flip_owner(game.positions['bot_left'], current_player, P1, P2)
    if game.positions['bot_right']['card'] is not None and played_card['r_value'] > game.positions['bot_right']['card']['l_value']:
        __flip_owner(game.positions['bot_right'], current_player, P1, P2)
    if game.positions['mid_center']['card'] is not None and played_card['t_value'] > game.positions['mid_center']['card']['b_value']:
        __flip_owner(game.positions['mid_center'], current_player, P1, P2)


def __bot_right_placement(game, played_card, current_player, P1, P2):
    if game.positions['bot_center']['card'] is not None and played_card['l_value'] > game.positions['bot_center']['card']['r_value']:
        __flip_owner(game.positions['bot_center'], current_player, P1, P2)
    if game.positions['mid_right']['card'] is not None and played_card['t_value'] > game.positions['mid_right']['card']['b_value']:
        __flip_owner(game.positions['mid_right'], current_player, P1, P2)


def __flip_owner(card, current_player, P1, P2):
    if card['current_owner'] != current_player.name:
        if card['current_owner'] == P1.name:
            card['current_owner'] = P2.name
        else:
            card['current_owner'] = P1.name
