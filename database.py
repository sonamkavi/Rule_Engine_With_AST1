# database.py

import sqlite3

def create_connection():
    connection = sqlite3.connect('rules.db')  # Create or connect to a SQLite database
    return connection

def create_table():
    connection = create_connection()
    with connection:
        connection.execute('''
            CREATE TABLE IF NOT EXISTS rules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rule_string TEXT NOT NULL,
                rule_ast TEXT -- JSON or serialized AST format
            );
        ''')
    connection.close()

def insert_rule(rule_string, rule_ast):
    connection = create_connection()
    with connection:
        connection.execute('''
            INSERT INTO rules (rule_string, rule_ast) VALUES (?, ?);
        ''', (rule_string, rule_ast))
    connection.close()

def fetch_rules():
    connection = create_connection()
    with connection:
        result = connection.execute('SELECT * FROM rules').fetchall()
    connection.close()
    return result
