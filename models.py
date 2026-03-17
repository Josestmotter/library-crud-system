class Book:
    def __init__(self, title, author, year, genre, quantity_in_storage, price):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.quantity_in_storage = quantity_in_storage
        self.price = price


class Reader:
    def __init__(self, name, email, phone_number, birthday, password):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.birthday = birthday
        self.password = password