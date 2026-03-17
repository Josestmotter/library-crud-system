class View:
    def __init__(self, system):
        self.system = system

    def show_books(self):
        books = self.system.search_books()

        if not books:
            print("\nNo books registered.\n")
            return

        print("\n--- BOOK LIST ---")
        for book in books:
            print(
                f"ID: {book[0]} | "
                f"Title: {book[1]} | "
                f"Author: {book[2]} | "
                f"Year: {book[3]} | "
                f"Genre: {book[4]} | "
                f"Quantity: {book[5]} | "
                f"Price: ${book[6]:.2f}"
            )
        print()

    def show_readers(self):
        readers = self.system.search_readers()

        if not readers:
            print("\nNo readers registered.\n")
            return

        print("\n--- READER LIST ---")
        for reader in readers:
            print(
                f"ID: {reader[0]} | "
                f"Name: {reader[1]} | "
                f"Email: {reader[2]} | "
                f"Phone: {reader[3]} | "
                f"Birthday: {reader[4]}"
            )
        print()