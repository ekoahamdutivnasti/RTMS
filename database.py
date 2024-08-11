import sqlite3

class DatabaseManager:
    def __init__(self, db_name='rtms.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._setup_db()

    def _setup_db(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY,
                user_input TEXT,
                ai_response TEXT,
                correct INTEGER
            )
        ''')
        self.connection.commit()

    def save_response(self, user_input, ai_response, correct):
        self.cursor.execute('''
            INSERT INTO responses (user_input, ai_response, correct)
            VALUES (?, ?, ?)
        ''', (user_input, ai_response, correct))
        self.connection.commit()

    def close(self):
        self.connection.close()
