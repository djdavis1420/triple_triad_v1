from src.services import utilities
from src.models import all_cards
from src.models.board import Board
from src.models.player import Player


def test_determine_player__should_return_p2():
    turn_count = 2
    P1 = Player()
    P2 = Player()
    starting_player = P1
    players = [P1, P2]

    actual = utilities.determine_player(turn_count, starting_player, players)

    assert actual is P2


def test_has_card_in_hand__should_return_true():
    player = Player()
    player.hand = [all_cards.COCKATRICE, all_cards.COCKATRICE, all_cards.COCKATRICE, all_cards.COCKATRICE, all_cards.BLOBRA]
    card = 'Blobra'

    actual = utilities.has_card_in_hand(player, card)

    assert actual is True


def test_has_card_in_hand__should_return_false():
    player = Player()
    player.hand = [all_cards.COCKATRICE, all_cards.COCKATRICE, all_cards.COCKATRICE, all_cards.COCKATRICE, all_cards.BLOBRA]
    card = 'Zell'

    actual = utilities.has_card_in_hand(player, card)

    assert actual is False


def test_position_is_available__should_return_true():
    game = Board()
    position = 'mid_center'

    actual = utilities.position_is_available(game, position)

    assert actual is True


def test_place_card__should_place_card_in_mid_center():
    game = Board()
    player = Player()
    card = all_cards.BLOBRA
    position = 'mid_center'

    actual = utilities.place_card(game, player, card, position)

    assert actual['mid_center']['card'] == all_cards.BLOBRA
