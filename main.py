from models import Reader, Book
from storage import System
from services import View


system = System()
view = View(system)

system.create_sql()


def register_book():
    print("\n--- REGISTER BOOK ---")
    title = input("Title: ").strip()
    author = input("Author: ").strip()

    try:
        year = int(input("Year: ").strip())
        quantity_in_storage = int(input("Quantity in storage: ").strip())
        price = float(input("Price: ").strip())
    except ValueError:
        print("Invalid value. Year and quantity must be integers, and price must be a number.\n")
        return

    genre = input("Genre: ").strip()

    book = Book(title, author, year, genre, quantity_in_storage, price)
    system.insert_book(book)
    print("Book registered successfully.\n")


def register_reader():
    print("\n--- REGISTER READER ---")
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    phone_number = input("Phone number: ").strip()
    birthday = input("Birthday: ").strip()
    password = input("Password: ").strip()

    reader = Reader(name, email, phone_number, birthday, password)
    system.insert_reader(reader)
    print("Reader registered successfully.\n")


def delete_book():
    view.show_books()

    try:
        book_id = int(input("Enter the book ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.\n")
        return

    system.delete_book_by_id(book_id)
    print()


def delete_reader():
    view.show_readers()

    try:
        reader_id = int(input("Enter the reader ID to delete: ").strip())
    except ValueError:
        print("Invalid ID.\n")
        return

    system.delete_reader_by_id(reader_id)
    print()


def menu():
    print("=--- LIBRARY MENU ---=")
    print("[1] Register book")
    print("[2] Register reader")
    print("[3] Delete book by ID")
    print("[4] Delete reader by ID")
    print("[5] Show books")
    print("[6] Show readers")
    print("[0] Exit")


while True:
    menu()
    action = input("Action: ").strip()

    if action == "1":
        register_book()

    elif action == "2":
        register_reader()

    elif action == "3":
        delete_book()

    elif action == "4":
        delete_reader()

    elif action == "5":
        view.show_books()

    elif action == "6":
        view.show_readers()

    elif action == "0":
        print("Program closed.")
        break

    else:
        print("Invalid option.\n")