import sqlite3


class Database:
    def __init__(self, path_to_db='users.db'):
        self.path_to_db = path_to_db

    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None,
                fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection()
        cursor = connection.cursor()
        data_sql = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchone:
            data_sql = cursor.fetchone()

        if fetchall:
            data_sql = cursor.fetchall()

        connection.close()

        return data_sql
    # id

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users(
        id NOT NULL UNIQUE
    );
"""
        self.execute(sql, commit=True)

    def create_user_id(self, chat_id):
        sql = """
        INSERT OR IGNORE INTO Users(id) VALUES(?) 
"""
        self.execute(sql, parameters=(chat_id,), commit=True)

    def create_table_users_name(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users_name(
        name TEXT UNIQUE
    );
"""
        self.execute(sql, commit=True)

    def get_all_users(self):
        sql = "SELECT id FROM Users"
        return self.execute(sql, fetchall=True)
