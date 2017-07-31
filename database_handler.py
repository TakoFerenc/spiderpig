import sqlite3
from contextlib import contextmanager


class HandleData:

    def __init__(self, database='data_for_urls.db'):
        self.database = database
        self.conn = None
        self.cursor = None
        self.create_database()

    def create_database(self):
        with self.connection_handler() as db:
            db.execute('CREATE TABLE IF NOT EXISTS links (urls TEXT PRIMARY KEY)')

    def write_data_to_db(self, urls):
        with self.connection_handler() as db:
            for url in urls:
                db.execute('INSERT OR IGNORE INTO links (urls) VALUES (?)', (url,))

    def read_data_from_db(self):
        with self.connection_handler() as db:
            db.execute('SELECT urls FROM links')
            rows = db.fetchall()
            for row in rows:
                yield row[0]

    @contextmanager
    def connection_handler(self):
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
            yield self.cursor
        except sqlite3.Error as error:
            print(error)
        finally:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()


