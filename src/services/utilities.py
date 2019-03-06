def determine_player(turn_count, starting_player, players):
    if turn_count % 2 != 0:
        player = [item for item in players if item == starting_player][0]
    else:
        player = [item for item in players if item != starting_player][0]
    return player


def has_card_in_hand(player, card):
    for item in player.hand:
        if card.upper() == item['name'].upper():
            return True
    return False


def position_is_available(game, position):
    if game.positions[position]['card'] is not None:
        return False
    else:
        return True


def place_card(game, player, card, position):
    for k, v in game.positions.items():
        if k == position:
            v['card'] = card
            v['original_owner'] = player.name
            v['current_owner'] = player.name
    return game.positions
