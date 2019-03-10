import os
import mysql.connector as MySQLdb
from src.models.all_cards import CARDS


def get_credentials():
    username = os.environ['database_username']
    password = os.environ['database_password']
    return username, password


def create_cards_table(username, password):
    conn = MySQLdb.connect(user=username, password=password, host='localhost', port='3306', database='tripletriad')
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS cards''')
    c.execute('''CREATE TABLE cards (id VARCHAR(4) UNIQUE PRIMARY KEY, card_name VARCHAR(50), element VARCHAR(25),
                t_value INT, b_value INT, l_value INT, r_value INT);''')
    for card in CARDS:
        card_values = (card['id'], card['name'], card['element'], card['t_value'], card['b_value'], card['l_value'], card['r_value'])
        command = '''INSERT INTO cards (id, card_name, element, t_value, b_value, l_value, r_value) VALUES (%s, %s, %s, %s, %s, %s, %s);'''
        c.execute(command, card_values)
    conn.commit()
    conn.close()
