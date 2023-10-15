from book import Book
import json
import os

def add_new_book(isbn, name, description, publish_year, author, price):

    newBook = Book(isbn, name, description, publish_year, author, price)

    newBook_dict = Book.to_dict(newBook)

    # reading current file directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, "books.json")
    
    all_books = []
    
    # checking if the path to the file exists and reading from it
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, 'r') as file:
            all_books = json.load(file)

    all_books.append(newBook_dict)
    
    # writing to the file
    with open(path, "w") as file:
        json.dump(all_books, file, indent=4)

def display_all_books(filename):

    # reading current file directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, filename)
    
    all_books = []
    
    # reading from the file
    with open(path, 'r') as file:
        all_books = json.load(file)
        
    # displaying all books
    print("All books: ")
    for element in all_books:
        print(element.get("name") + "\n")

    book_names = [element.get("name") for element in all_books]

    return book_names

def display_lower_price(filename, price):
    # reading current file directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, filename)
    
    all_books = []
    
    # reading from the file
    with open(path, 'r') as file:
        all_books = json.load(file)

    lower_priced_books = []
        
    # displaying books lower than the input
    print("Books lower than chosen price: ")
    for element in all_books:
        # checking the user input
        if element.get("price") < price:
            lower_priced_books.append(element.get("name"))
            print (element.get("name") + "\n")

    return lower_priced_books

def display_higher_price(filename, price):

    # reading current file directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, filename)
    
    all_books = []
    
    # reading from the file
    with open(path, 'r') as file:
        all_books = json.load(file)

    higher_priced_books = []
        
    # displaying books higher than input
    print("Books higher than chosen price: ")
    for element in all_books:
        # checking the user input
        if element.get("price") > price:
            higher_priced_books.append(element.get("name"))
            print(element.get("name") + "\n")

    return higher_priced_books

def display_author_books(filename, author):

    # reading current file directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, filename)
    
    all_books = []
    
    # reading from the file
    with open(path, 'r') as file:
        all_books = json.load(file)

    author_books = []
        
    # displaying books with chosen author
    print("Books with chosen author: ")
    for element in all_books:
        # checking the user input
        if element.get("author") == author:
            author_books.append(element.get("name"))
            print(element.get("name") + "\n")

    return author_books

def display_lower_year(filename, publish_year):

    # reading current file directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, filename)
    
    all_books = []
    
    # reading from the file
    with open(path, 'r') as file:
        all_books = json.load(file)

    lower_year_books = []
        
    # displaying books with chosen author
    print("Books with publish year lower than chosen: ")
    for element in all_books:
        # checking the user input
        if element.get("publish_year") < publish_year:
            lower_year_books.append(element.get("name"))
            print(element.get("name") + "\n")

    return lower_year_books

def display_higher_year(filename, publish_year):

    # reading current file directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_directory, filename)
    
    all_books = []
    
    # reading from the file
    with open(path, 'r') as file:
        all_books = json.load(file)

    higher_year_books = []
        
    # displaying books with chosen author
    print("Books with publish year higher than chosen: ")
    for element in all_books:
        # checking the user input
        if element.get("publish_year") > publish_year:
            higher_year_books.append(element.get("name"))
            print(element.get("name") + "\n")

    return higher_year_books

# add_new_book(1, "bookname", "description", 2018, "author", 29.99)

# display_all_books("books.json")

# display_lower_price("books.json", price)

# display_higher_price("books.json", price)

# display_author_books("books.json", author)

# display_lower_year("books.json", publish_year)

# display_higher_year("books.json", publish_year)
