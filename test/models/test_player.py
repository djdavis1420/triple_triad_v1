from src.models.player import Player


def test_generate_deck__should_generate_full_deck():
    # no arrange

    actual = Player()

    assert len(actual.deck) == 110


def test_generate_hand__should_generate_hand_of_five_cards():
    # no arrange

    actual = Player().generate_hand()

    assert len(actual) == 5
