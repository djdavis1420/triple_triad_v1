import mysql.connector as MySQLdb
from src.models.all_cards import CARDS


def create_cards_table(db_username, db_password):
    conn = MySQLdb.connect(user=db_username, password=db_password, host='localhost', port='3306', database='triple_triad')
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS cards;''')
    c.execute('''CREATE TABLE cards (id VARCHAR(4) UNIQUE PRIMARY KEY, card_name VARCHAR(50), element VARCHAR(25),
                t_value INT, b_value INT, l_value INT, r_value INT);''')
    for card in CARDS:
        card_values = (card['id'], card['name'], card['element'], card['t_value'], card['b_value'], card['l_value'], card['r_value'])
        command = '''INSERT INTO cards (id, card_name, element, t_value, b_value, l_value, r_value) VALUES (%s, %s, %s, %s, %s, %s, %s);'''
        c.execute(command, card_values)
    conn.commit()
    conn.close()


def create_players_table(db_username, db_password):
    conn = MySQLdb.connect(user=db_username, password=db_password, host='localhost', port='3306', database='triple_triad')
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS players;''')
    c.execute('''CREATE TABLE players (id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
                user_name VARCHAR(50) UNIQUE NOT NULL, first_name VARCHAR(50) NOT NULL,
                preferred_difficulty VARCHAR(10) DEFAULT 'easy');''')
    conn.commit()
    conn.close()


def create_decks_table(db_username, db_password):
    conn = MySQLdb.connect(user=db_username, password=db_password, host='localhost', port='3306', database='triple_triad')
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS decks;''')
    c.execute('''CREATE TABLE decks (player_id INT NOT NULL, card_id VARCHAR(4) NOT NULL,
                quantity INT NOT NULL DEFAULT 0, FOREIGN KEY (player_id) REFERENCES players(id),
                FOREIGN KEY (card_id) REFERENCES cards(id));''')
    conn.commit()
    conn.close()
