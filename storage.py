import sqlite3
from pathlib import Path


class System:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def open_sql(self):
        base_dir = Path(__file__).resolve().parent
        db_path = base_dir / "data" / "books_and_readers.db"

        db_path.parent.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def save_sql(self):
        self.connection.commit()

    def close_sql(self):
        if self.connection:
            self.connection.close()

    def create_sql(self):
        cursor = self.open_sql()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS readers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                birthday TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL,
                genre TEXT NOT NULL,
                quantity_in_storage INTEGER NOT NULL,
                price REAL NOT NULL
            )
        """)

        self.save_sql()
        self.close_sql()

    def insert_book(self, book_object):
        cursor = self.open_sql()

        cursor.execute("""
            INSERT INTO books (title, author, year, genre, quantity_in_storage, price)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            book_object.title,
            book_object.author,
            book_object.year,
            book_object.genre,
            book_object.quantity_in_storage,
            book_object.price
        ))

        self.save_sql()
        self.close_sql()

    def insert_reader(self, reader_object):
        cursor = self.open_sql()

        cursor.execute("""
            INSERT INTO readers (name, email, phone_number, birthday, password)
            VALUES (?, ?, ?, ?, ?)
        """, (
            reader_object.name,
            reader_object.email,
            reader_object.phone_number,
            reader_object.birthday,
            reader_object.password
        ))

        self.save_sql()
        self.close_sql()

    def search_books(self):
        cursor = self.open_sql()
        cursor.execute("SELECT * FROM books ORDER BY id")
        data = cursor.fetchall()
        self.close_sql()
        return data

    def search_readers(self):
        cursor = self.open_sql()
        cursor.execute("SELECT * FROM readers ORDER BY id")
        data = cursor.fetchall()
        self.close_sql()
        return data

    def delete_book_by_id(self, book_id):
        cursor = self.open_sql()

        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()

        if not book:
            print("Book not found.")
            self.close_sql()
            return

        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        self.save_sql()
        self.close_sql()
        print("Book deleted successfully.")

    def delete_reader_by_id(self, reader_id):
        cursor = self.open_sql()

        cursor.execute("SELECT * FROM readers WHERE id = ?", (reader_id,))
        reader = cursor.fetchone()

        if not reader:
            print("Reader not found.")
            self.close_sql()
            return

        cursor.execute("DELETE FROM readers WHERE id = ?", (reader_id,))
        self.save_sql()
        self.close_sql()
        print("Reader deleted successfully.")