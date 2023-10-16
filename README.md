# Book Manager Application

A simple command-line book management application with basic functionalities such as adding new books, displaying all books, and various other filtering options.

## Installation

To use the Book Manager Application, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/patrikinho0/third-assignment-patrikinho0.git
   ```

2. Run the application using your IDE terminal in the main.py file.

## Files

The application consists of the following files:

1. `main.py`: Contains the main logic and user interface for the Book Manager Application.
2. `utils.py`: Includes various utility functions to support the main functionality of the application.
3. `test.py`: Contains unit tests to ensure the proper functioning of the application.
4. `book.py`: Defines the Book class used in the application.

## Functionality

The application allows users to perform the following operations:
<br><br>

- Add a new book.
   - python3 utils.py add_new_book(ISBN, name, description, publish_year, author, price)

- Display all books.
  - python3 utils.py display_all_books(filename)

- Display books with prices lower than the input.
  - python3 utils.py display_lower_price(filename, price)

- Display books with prices higher than the input.
  - python3 utils.py display_higher_price(filename, price)

- Display books by a specific author.
  - python3 utils.py display_author_books(filename, author)

- Display books published before a specific year.
  - python3 utils.py display_lower_year(filename, publish_year)

- Display books published after a specific year.
  - python3 utils.py display_higher_year(filename, publish_year)
<br><br>
## Manual testing

The application allows the user to test the application manually:

Step 1. Clone the repository:
   ```
   git clone https://github.com/patrikinho0/third-assignment-patrikinho0.git
   ```

Step 2. Go into the utils.py file

Step 3. Uncomment the following functions and fill the example arguments within your liking:
```py
# add_new_book(1, "bookname", "description", 2018, "author", 29.99)

# display_all_books("books.json")

# display_lower_price("books.json", price)

# display_higher_price("books.json", price)

# display_author_books("books.json", author)

# display_lower_year("books.json", publish_year)

# display_higher_year("books.json", publish_year)
```

<br>

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/PblptkeH)

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12231646&assignment_repo_type=AssignmentRepo)

<p align="center">Made by: <a href="https://github.com/patrikinho0">patrikinho0</a></p>
