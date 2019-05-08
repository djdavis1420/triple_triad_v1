from src.database import database


def test_get_credentials__should_get_login_information():
    db_username, db_password = database.get_credentials()

    actual = database.get_credentials()

    assert actual == (db_username, db_password)


def test_check_for_player__should_check_database_for_player_username():
    db_username, db_password = database.get_credentials()
    username = ('djdavis1420',)

    actual = database.check_for_player(db_username, db_password, username)

    assert actual[0][1] == 'djdavis1420'


def test_create_player__should_create_new_player():
    db_username, db_password = database.get_credentials()
    new_user = ('djdavis1420', 'Dylan', 'medium')

    database.create_player(db_username, db_password, new_user)

    pass

