from src.database import database
from src.database import table_creation


def test_create_cards_table__should_create_cards_table():
    db_username, db_password = database.get_credentials()

    table_creation.create_cards_table(db_username, db_password)

    pass


def test_create_players_table__should_create_players_table():
    db_username, db_password = database.get_credentials()

    table_creation.create_players_table(db_username, db_password)

    pass


def test_create_decks_table__should_create_decks_table():
    db_username, db_password = database.get_credentials()

    table_creation.create_decks_table(db_username, db_password)

    pass
