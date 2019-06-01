import os
import mysql.connector as MySQLdb


def get_credentials():
    db_username = os.environ['database_username']
    db_password = os.environ['database_password']
    return db_username, db_password


def check_for_player(db_username, db_password, username):
    conn = MySQLdb.connect(user=db_username, password=db_password, host='localhost', port='3306', database='triple_triad')
    c = conn.cursor()
    query = '''SELECT * FROM players WHERE user_name = %s;'''
    c.execute(query, username)
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result


def create_player(db_username, db_password, new_user):
    conn = MySQLdb.connect(user=db_username, password=db_password, host='localhost', port='3306', database='triple_triad')
    c = conn.cursor()
    command = '''INSERT INTO players (user_name, first_name, preferred_difficulty) VALUES (%s, %s, %s);'''
    c.execute(command, new_user)
    conn.commit()
    conn.close()

