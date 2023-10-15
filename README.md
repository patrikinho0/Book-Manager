# Book Manager Application

A simple command-line book management application with basic functionalities such as adding new books, displaying all books, and various other filtering options.

## Installation

To use the Book Manager Application, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/patrikinho0/third-assignment-patrikinho0.git
   ```

3. Run the application using your IDE terminal.

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
  - python3 utils.py display_all_books()

- Display books with prices lower than the input.
  - python3 utils.py display_lower_price(price)

- Display books with prices higher than the input.
  - python3 utils.py display_higher_price(price)

- Display books by a specific author.
  - python3 utils.py display_author_books(author)

- Display books published before a specific year.
  - python3 utils.py display_lower_year(publish_year)

- Display books published after a specific year.
  - python3 utils.py display_higher_year(publish_year)
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

# display_all_books()

# display_lower_price(price)

# display_higher_price(price)

# display_author_books(author)

# display_lower_year(publish_year)

# display_higher_year(publish_year)
```


<br>

<p align="center">Made by: <a href="https://github.com/patrikinho0">patrikinho0</a></p>
