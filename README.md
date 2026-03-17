# Library CRUD System

A simple terminal-based CRUD system built with Python and SQLite for managing books and readers in a library.

## Features

- Register books
- Register readers
- List all books
- List all readers
- Delete books by ID
- Delete readers by ID
- Store data with SQLite

## Technologies Used

- Python
- SQLite3

## Project Structure

```bash
library/
├── data/
│   └── books_and_readers.db
├── main.py
├── models.py
├── services.py
├── storage.py
├── README.md
└── .gitignore

## How to Run

1. Clone this repository
2. Open the project folder
3. Run the command below:

```bash
python main.py
```

 Library CRUD System

## Example Menu
```text
=--- LIBRARY MENU ---=
[1] Register book
[2] Register reader
[3] Delete book by ID
[4] Delete reader by ID
[5] Show books
[6] Show readers
[0] Exit
```
## Learning Goals

- Practice Python fundamentals with a real-world project
- Learn how CRUD operations work in practice
- Understand how to integrate Python with SQLite
- Improve code organization using separate files and modules
- Strengthen logic, data manipulation, and terminal-based interaction

## Future Improvements

- Add update functionality for books and readers
- Improve input validation and error handling
- Add borrowing and returning book features
- Implement a more advanced search system
- Build a graphical interface for easier use
- Export data to files such as CSV or JSON
